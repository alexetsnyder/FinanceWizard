#FinWizExec

from os import system
from sys import platform
from FinWizData import *
from FinWizEnum import *
from FinWizExcept import ArgumentError
from FinWizDataModel import Expense, Revenue, Date

def exec_quit():
	raise SystemExit

def exec_clear():
	if platform == 'win32':
		system('cls')
	elif platform == 'linux':
		system('clear')
	else:
		print('Lazy programmer need to look up more cases for os.platform...')

#Add Command
def exec_add_expense(date, name, cost, category, source):
	RUNTIME_DATA[CURRENT_USER][eRunTimeKey.EXPENSE].append(Expense(Date(date), name, cost, category, MONEY_SOURCE[source]))

def exec_add_revenue(date, source, amount):
	RUNTIME_DATA[CURRENT_USER][eRunTimeKey.REVENUE].append(Revenue(Date(date), MONEY_SOURCE[source], amount))

#Print Command
def exec_print_revenue(*args):
	print('Revenue: ')
	for rev in RUNTIME_DATA[CURRENT_USER][eRunTimeKey.REVENUE]:
		print(rev)

def exec_print_expense(*args):
	print('Expenses: ')
	for exp in RUNTIME_DATA[CURRENT_USER][eRunTimeKey.EXPENSE]:
		print(exp)

EXEC_TABLE = {

	eInputCommand.QUIT  : {
		eInputControl.NO_ARGS : exec_quit
	},

	eInputCommand.CLEAR : {
		eInputControl.NO_ARGS : exec_clear
	},

	eInputCommand.SET   : {
		eInputControl.EXP : exec_add_expense,
		eInputControl.REV : exec_add_revenue
	},

	eInputCommand.PRINT : {
		eInputControl.EXP : exec_print_expense,
		eInputControl.REV : exec_print_revenue
	}
}
