#FinWizExec

import re
import os
import sys
from FinWizData import *
import FinWizHelperFunc as  fwHelp
import FinWizExcept as fwExcept
import FinWizDataModel as fwDataModel
 
#Parse Arguments
func_sym_str  = '-'
data_sym_str  = ':'
ident_str     = '[A-Za-z][A-Za-z0-9\_]*'
data_str      = data_sym_str + ident_str 
rec_data_str  = data_str + '(' + data_str + ')*'
func_str      = func_sym_str + ident_str + '(' + data_str + ')*'

rec_data_re   = re.compile(rec_data_str) 
func_re       = re.compile(func_str)

def gen_data_keys(dataKeys):
	prv_index = index = 0
	while index != -1:
		index = dataKeys.find(':', prv_index+1)
		if index == -1:
			yield DATA_KEYS[dataKeys[prv_index:]]
		else:
			yield DATA_KEYS[dataKeys[prv_index:index]]
		prv_index = index

def parse_func_and_data(funcAndData):
	prv_index = 0
	index = funcAndData.find(':', prv_index)
	if index == -1:
		return (FUNCTIONS[funcAndData[prv_index:]], [])
	return (FUNCTIONS[funcAndData[prv_index:index]], [data for data in gen_data_keys(funcAndData[index:])])

def gen_args(*args):
	i = 0
	while i < len(args):
		if func_re.fullmatch(args[i]):
			control = parse_func_and_data(args[i])
			for j in range(len(args[i+1:])):
				if func_re.fullmatch(args[j+i+1]):
					yield (control, args[i+1:j+i+1])
					i = j + i + 1
					break
			else:
				yield (control, args[i+1:])
				break
		elif rec_data_re.fullmatch(args[i]):
			control = [data for data in gen_data_keys(args[i])]
			for j in range(len(args[i+1:])):
				if rec_data_re.fullmatch(args[j+i+1]) or func_re.fullmatch(args[j+i+1]):
					yield(control, args[i+1:j+i+1])
					i = j + i + 1
					break
			else:
				yield (control, args[i+1:])
				break
		else:
			break

#Quit Command
def exec_quit():
	raise SystemExit

#Clear Command
def exec_clear():
	if sys.platform == 'win32':
		os.system('cls')
	elif sys.platform == 'linux':
		os.system('clear')
	else:
		print('Lazy programmer need to look up more cases for os.platform...')

#Add Command
def exec_add(control, *args):
	i = 0
	for data in control:
		item = None
		if data == eDataKey.EXP:
			item = fwDataModel.Expense(fwDataModel.Date(args[i]), args[i+1], args[i+2], args[i+3], MONEY_SOURCE[args[i+4]])
			i += 5
		elif data == eDataKey.REV:
			item = fwDataModel.Revenue(fwDataModel.Date(args[i]), MONEY_SOURCE[args[i+1]], args[i+2])
			i += 3
		else:
			raise fwExcept.ControlError('exec_add', control)

		RUNTIME_DATA[CURRENT_USER][data].append(item)

#Print Command
def exec_print(control):
	for data in control:
		for x in RUNTIME_DATA[CURRENT_USER][data]:
			print(x)

#Import Command
def exec_import(control, *args):
	for i, fileKey in enumerate(control):
		if not fileKey == eDataKey.FILE:
			raise fwExcept.ControlError('exec_import', fileKey)	
		with open(args[i], 'r') as dataFile:
			for line in dataFile:
				inputList = fwHelp.input_to_list(line)
				exec_command(eInputCommand.SET, inputList)

#Exec Table
EXEC_TABLE = {

	eInputCommand.QUIT   : exec_quit,
	eInputCommand.CLEAR  : exec_clear,
	eInputCommand.SET    : exec_add,
	eInputCommand.PRINT  : exec_print,
	eInputCommand.IMPORT : exec_import
}

#Main Exec Command Function
def exec_command(command, inputList):
	try:
		loopRanOnceFlag = False
		for control, arglist in gen_args(*inputList):
			if arglist:
				EXEC_TABLE[command](control, *arglist)
			else:
				EXEC_TABLE[command](control)
			loopRanOnceFlag = True

		if not loopRanOnceFlag:
			EXEC_TABLE[command]()

	except KeyError as keyError:
	 	print('Error: In exec_command: Command not found in EXEC_TABLE...')
	 	print('key:', keyError)
	except TypeError:
		print('Error: Incorrect number of arguments...')
	except ValueError:
		print('Error: Used a character when a number was required...')
	except IndexError:
		print('Error: Wrong number of arguments...')
	except fwExcept.ArgumentError as argError:
		print(argError.message)
	except fwExcept.DateError as dateError:
		print(dateError.message)

