#FinWizData

from FinWizEnum import *

COMMANDS = {
	'load'  : eInputCommand.LOAD,
	'save'  : eInputCommand.SAVE,
	'add'   : eInputCommand.SET,
	'read'  : eInputCommand.GET,
	'print' : eInputCommand.PRINT,
	'p'     : eInputCommand.PRINT,

	'clear' : eInputCommand.CLEAR,
	'cls'   : eInputCommand.CLEAR,
	'reset' : eInputCommand.CLEAR,

	'quit'  : eInputCommand.QUIT,
	'q'     : eInputCommand.QUIT,
	'end'   : eInputCommand.QUIT,
	'exit'  : eInputCommand.QUIT
}

CONTROLS = {
	''     : eInputControl.NO_ARGS,
	'-exp' : eInputControl.EXP,
	'-rev' : eInputControl.REV 
}

MONEY_SOURCE = {
	'cash'  : eMoneySource.CASH,
	'bank'  : eMoneySource.BANK,
	'work'  : eMoneySource.WORK,
	'extra' : eMoneySource.EXTRA
}

SOURCE_TO_STRING = {
	eMoneySource.CASH    : 'cash',
	eMoneySource.BANK    : 'bank',
	eMoneySource.WORK    : 'work',
	eMoneySource.EXTRA   : 'revenue'
}

DATE_LOOKUP_TABLE = {
	eDateFormat.BIG_ENDIAN : { 
		ePlace.FIRST  : eDate.YEAR,
		ePlace.SECOND : eDate.MONTH,
		ePlace.THIRD  : eDate.DAY
	},
	eDateFormat.MIDDLE_ENDIAN : { 
		ePlace.FIRST  : eDate.MONTH,
		ePlace.SECOND : eDate.DAY,
		ePlace.THIRD  : eDate.YEAR 
	},
	eDateFormat.LITTLE_ENDIAN : { 
		ePlace.FIRST  : eDate.DAY,
		ePlace.SECOND : eDate.MONTH,
		ePlace.THIRD  : eDate.YEAR
	}
}

INT_TO_MONTH = {
	1  : eMonth.JANUARY,
	2  : eMonth.FEBRUARY,
	3  : eMonth.MARCH,
	4  : eMonth.APRIL,
	5  : eMonth.MAY,
	6  : eMonth.JUNE,
	7  : eMonth.JULY,
	8  : eMonth.AUGUST,
	9  : eMonth.SEPTEMBER,
	10 : eMonth.OCTOBER,
	11 : eMonth.NOVEMBER,
	12 : eMonth.DECEMBER
}

MONTH_TO_INT = {
	eMonth.JANUARY   : 1,
	eMonth.FEBRUARY  : 2,
	eMonth.MARCH     : 3,
	eMonth.APRIL     : 4,
	eMonth.MAY       : 5,
	eMonth.JUNE      : 6,
	eMonth.JULY      : 7,
	eMonth.AUGUST    : 8,
	eMonth.SEPTEMBER : 9,
	eMonth.OCTOBER   : 10,
	eMonth.NOVEMBER  : 11,
	eMonth.DECEMBER  : 12
}

DAYS_IN_MONTH = {
	eMonth.JANUARY   : 31,
	eMonth.FEBRUARY  : 28,
	eMonth.MARCH     : 31,
	eMonth.APRIL     : 30,
	eMonth.MAY       : 31,
	eMonth.JUNE      : 30,
	eMonth.JULY      : 31,
	eMonth.AUGUST    : 31,
	eMonth.SEPTEMBER : 30,
	eMonth.OCTOBER   : 31,
	eMonth.NOVEMBER  : 30,
	eMonth.DECEMBER  : 31
}

CURRENT_USER = 'Admin'
DATE_FORMAT = eDateFormat.MIDDLE_ENDIAN

RUNTIME_DATA = { 
	CURRENT_USER : {
		eRunTimeKey.EXPENSE : [],
		eRunTimeKey.REVENUE : []
	}
}