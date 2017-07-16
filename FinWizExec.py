#FinWizExec

from os import system
from sys import platform
from FinWizExcept import ArgumentError
from FinWizData import RUNTIME_DATA, CURRENT_USER, MONEY_SOURCE
from FinWizEnum import eInputCommand, eMoneySource, eDateFormat, eRunTimeKey
from FinWizDataModel import Expense, Revenue, Date

def arg_exec_list(*args):
	grouped_exec = []
	for i in range(len(args)):
		if args[i][0] == '-':
			for j in range(i, len(args)):
				if j == len(args)-1 or args[j+1][0] == '-':
					grouped_exec.append([args[i], args[i+1:j+1]])
					break
	return grouped_exec

def exec_quit(*args):
	raise SystemExit

def exec_clear(*args):
	if platform == 'win32':
		system('cls')
	elif platform == 'linux':
		system('clear')
	else:
		print('Lazy programmer need to look up more cases for os.platform...')

def exec_expense(*args):
	if len(args) != 5:
		raise ArgumentError('exec_expense', 'Arguments provided: ' + str(len(args)) + ' Arguments required: 5')

	tmpExpense = Expense(Date(eDateFormat.MIDDLE_ENDIAN, args[0]), args[1], float(args[2]), args[3], MONEY_SOURCE[args[4]])
	RUNTIME_DATA[CURRENT_USER][eRunTimeKey.EXPENSE].append(tmpExpense)

def exec_revenue(*args):
	if len(args) != 3:
		raise ArgumentError('exec_revenue', 'Arguments provided: ' + str(len(args)) + ' Arguments required: 3')

	tmpRevenue = Revenue(Date(eDateFormat.MIDDLE_ENDIAN, args[0]), MONEY_SOURCE[args[1]], float(args[2]))
	RUNTIME_DATA[CURRENT_USER][eRunTimeKey.REVENUE].append(tmpRevenue)

def print_expense(*args):
	print('Expenses: ')
	for exp in RUNTIME_DATA[CURRENT_USER][eRunTimeKey.EXPENSE]:
		print(exp)

def print_revenue(*args):
	print('Revenue: ')
	for rev in RUNTIME_DATA[CURRENT_USER][eRunTimeKey.REVENUE]:
		print(rev)

EXEC_ARG_TABLE = {
	eInputCommand.SET : {
		'-exp' : exec_expense,
		'-rev' : exec_revenue
	},
	eInputCommand.PRINT : {
		'-exp' : print_expense,
		'-rev' : print_revenue
	}
}

def exec_command(command, *args):
	exec_arg_list = arg_exec_list(*args)
	for exec_arg in exec_arg_list:
		try:
			EXEC_ARG_TABLE[command][exec_arg[0]](*exec_arg[1])
		except KeyError as keyError:
			print(keyError)
			raise ArgumentError('exec', exec_arg[0])


EXEC_TABLE = {
	eInputCommand.QUIT  : exec_quit,
	eInputCommand.CLEAR : exec_clear,
	eInputCommand.SET   : exec_command,
	eInputCommand.PRINT : exec_command
}
