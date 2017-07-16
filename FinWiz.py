#FinWiz

from FinWizEnum import eInputCommand 
from FinWizData import COMMANDS
from FinWizExec import EXEC_TABLE
from FinWizExcept import ParseError, ExecError, ArgumentError

def print_prompt():
	print('fin> ', end='')

def enter_input():
	return input()

def clean_input(userInput):
	return userInput.strip()

def input_to_list(cleanInput):
	return cleanInput.split()

def parse_input(inputList):
	command = eInputCommand.NULL
	try:
		command = COMMANDS[inputList[0]]
	except KeyError:
		raise ParseError('Error: In parse_input: Command not found in COMMANDS...')
	except IndexError:
		command = eInputCommand.EMPTY
	return command

def fin_wiz_exec(command, inputList):
	try:
		EXEC_TABLE[command](*inputList)
	except KeyError:
		raise ExecError('Error: In fin_wiz_exec: Command not found in EXEC_TABLE...')

def main_loop():
	while True:
		print_prompt()
		userInput = enter_input()
		cleanInput = clean_input(userInput)
		inputList = input_to_list(cleanInput)

		try:
			command = parse_input(inputList)
			if command == eInputCommand.EMPTY:
				continue
		except ParseError as parseError:
			print(parseError)
			continue

		try:
			fin_wiz_exec(command, inputList[1:])
		except ExecError as execError:
			print(execError.message)
		except ArgumentError as argError:
			print(argError.message)
		except SystemExit:
			break

if __name__ == '__main__':
	main_loop()
	print('Get a job!')
