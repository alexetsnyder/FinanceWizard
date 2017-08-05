#FinWiz

import readline
from FinWizData import *
import FinWizExec as fwExec
import FinWizHelperFunc as fwHelp
import FinWizDataModel as fwDM

def login():
	while True:
		user = input('Enter Username: ')
		fwExec.current_runtime = fwDM.Runtime(user)
		if user == 'admin':
			break
		try:
			fwExec.exec_import([eDataKey.USER]) 
			break
		except FileNotFoundError:
			choice = input('Are you a new user? ').lower()
			if choice == 'yes' or choice == 'y':
				break
			fwExec.current_runtime.remove(user)

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

def logout():
	if fwExec.current_runtime.user() == 'admin':
		return
	fwExec.exec_export([eDataKey.USER])

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
	login()
	main_loop()
	logout()
	print('Get a job!')
