#FinWizEnum

from enum import Enum

class eInputCommand(Enum):
	NULL    = 0
	INVALID = 1
	EMPTY   = 2
	IMPORT  = 3
	EXPORT  = 4
	QUIT    = 5
	SET     = 7
	GET     = 8
	PRINT   = 9
	DELETE  = 10
	CLEAR   = 11

class eArgFunction(Enum):
	NULL = 0
	SUM  = 1
	ALL  = 2
	SOME = 3
	ONE  = 4

class eDataKey(Enum):
	NULL    = 0
	EXP     = 1
	REV     = 2
	BANK    = 3
	DATE    = 4	
	USER    = 5
	FILE    = 6

class eMoneySource(Enum):
	NULL  = 0
	BANK  = 1
	CASH  = 2
	WORK  = 3
	EXTRA = 4

class eDateFormat(Enum):
	NULL          = 0
	BIG_ENDIAN    = 1		#(year, month, day)
	MIDDLE_ENDIAN = 2		#(month, day, year)
	LITTLE_ENDIAN = 3		#(day, month, year)

class eDate(Enum):
	NULL  = 0
	YEAR  = 1
	MONTH = 2
	DAY   = 3

class eMonth(Enum):
	NULL      = 0
	JANUARY   = 1
	FEBRUARY  = 2
	MARCH     = 3
	APRIL     = 4
	MAY       = 5
	JUNE      = 6
	JULY      = 7
	AUGUST    = 8
	SEPTEMBER = 9
	OCTOBER   = 10
	NOVEMBER  = 11
	DECEMBER  = 12

class ePlace(Enum):
	NULL   = 0
	FIRST  = 1
	SECOND = 2
	THIRD  = 3 

class eNull(Enum):
	INT = 0
	STR = 1

