#FinWiz

import readline
from FinWizEnum import *
from FinWizData import *
from FinWizExec import EXEC_TABLE
from FinWizExcept import ParseError, ExecError, ArgumentError

def print_prompt():
	return input('fwc> ')

def clean_input(userInput):
	return userInput.strip()

def input_to_list(cleanInput):
	inputList = cleanInput.split()
	arg_list = []
	index = 0
	while index < len(inputList):
		if inputList[index][0] == '\'' or inputList[index][0] == '\"':
			for j in range(index, len(inputList)):
				if inputList[j][-1] == '\'' or inputList[j][-1] == '\"':
					arg_list.append(' '.join(inputList[index:j+1])[1:-1])
					index = j + 1
					break
		else:
			arg_list.append(inputList[index])
			index += 1
	return arg_list

def parse_input(inputList):
	command = eInputCommand.NULL
	try:
		command = COMMANDS[inputList[0]]
	except KeyError:
		print('Error: In parse_input: Command not found in COMMANDS...')
		command = eInputCommand.INVALID
	except IndexError:
		command = eInputCommand.EMPTY
	return command

def parse_args(*args):
	i = 0
	while i < len(args):
		if args[i][0] == '-':
			for j in range(i, len(args)):
				if j == len(args)-1 or args[j+1][0] == '-':
					yield (CONTROLS[args[i]], args[i+1:j+1])
					i = j + 1 
					break
		else:
			raise ArgumentError('parse_args', 'Args without a control.')

def fin_wiz_exec(command, inputList):
	try:
		loopRanOnceFlag = False
		for control, arglist in parse_args(*inputList):
			EXEC_TABLE[command][control](*arglist)
			loopRanOnceFlag = True

		if not loopRanOnceFlag:
			EXEC_TABLE[command][eInputControl.NO_ARGS]()

	except KeyError:
	 	print('Error: In fin_wiz_exec: Command not found in EXEC_TABLE...')
	except ArgumentError as argError:
		print(argError.message)

def main_loop():
	while True:
		userInput = print_prompt()
		cleanInput = clean_input(userInput)
		inputList = input_to_list(cleanInput)

		command = parse_input(inputList)
		if command == eInputCommand.EMPTY or command == eInputCommand.INVALID:
			continue

		try:
			fin_wiz_exec(command, inputList[1:])
		except SystemExit:
			break

if __name__ == '__main__':
	main_loop()
	print('Get a job!')
