#FinWiz

import readline
from FinWizData import *
import FinWizExec as fwe
import FinWizExec as fwExec
import FinWizHelperFunc as fwHelp

def print_prompt():
	return input('fwc> ')

def clean_input(userInput):
	return userInput.strip()

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
	fwExec.exec_command(command, inputList)

def main_loop():
	while True:
		userInput = print_prompt()
		cleanInput = clean_input(userInput)
		inputList = fwHelp.input_to_list(cleanInput)

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
