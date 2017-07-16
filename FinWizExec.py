#FinWizExec

from os import system
from sys import platform
from FinWizEnum import eInputCommand
from FinWizExcept import ArgumentError

def arg_exec_list(*args):
	grouped_exec = []
	for i in range(len(args)):
		if args[i][0] == '-':
			for j in range(i, len(args)):
				if j == len(args)-1 or args[j+1][0] == '-':
					grouped_exec.append([args[i], args[i+1:j+1]])
					break
	return grouped_exec

def quit_loop(*args):
	raise SystemExit

def clear(*args):
	if platform == 'win32':
		system('cls')
	elif platform == 'linux':
		system('clear')
	else:
		print('Lazy programmer need to look up more cases for os.platform...')

def exec_expense(*args):
	print('Expense:', args)

def exec_revenue(*args):
	print('Revenue:', args)

SET_TABLE = {
	'-exp' : exec_expense,
	'-rev' : exec_revenue
}

def exec_set(*args):
	exec_arg_list = arg_exec_list(*args)
	for exec_arg in exec_arg_list:
		try:
			SET_TABLE[exec_arg[0]](*exec_arg[1])
		except KeyError:
			raise ArgumentError('exec_set', exec_arg[0])

EXEC_TABLE = {
	eInputCommand.QUIT  : quit_loop,
	eInputCommand.CLEAR : clear,
	eInputCommand.SET   : exec_set
}

if __name__ == '__main__':
	while True:
		userInput = input("Enter arg list: ")
		if userInput == 'q':
			break
		userInputList = userInput.split()
		try:
			EXEC_TABLE[eInputCommand.SET](*userInputList)
		except ArgumentError as ae:
			print(ae.message)