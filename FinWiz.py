#FinWiz

from FinWizEnum import *
from FinWizData import COMMANDS

def print_prompt():
	print('fin> ', end='')

def enter_input():
	return input()

def clean_input(userInput):
	return userInput.strip()

def parse_input(cleanInput):
	command = eInputCommand.NULL	
	try:
		command = COMMANDS[cleanInput]
	except KeyError:
		command = eInputCommand.INVALID
	return command 

def execute(parseData):
	if parseData == eInputCommand.INVALID:
		print("Incorrect Command! Try Again...")	
	elif parseData == eInputCommand.LOAD:
		print('Loading file...')
	elif parseData == eInputCommand.SAVE:
		print('Saving file...')
	return parseData

def main_loop():
	while True:
		print_prompt()
		userInput = enter_input()
		cleanInput = clean_input(userInput)
		command = parse_input(cleanInput)
		quit = execute(command)
		if quit == eInputCommand.QUIT:
			return
		elif quit == eInputCommand.NULL:
			print('Command returned as NULL, that shouldn\'t happen')


if __name__ == '__main__':
	main_loop()
	print('Get a job!')
