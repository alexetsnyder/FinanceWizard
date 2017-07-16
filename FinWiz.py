#FinWiz

import readline
from FinWizEnum import eInputCommand 
from FinWizData import COMMANDS, RUNTIME_DATA
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

def fin_wiz_exec(command, inputList):
	try:
		EXEC_TABLE[command](command, *inputList)
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
