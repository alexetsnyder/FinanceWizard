#FinWizEnum

from enum import Enum

class eInputCommand(Enum):
	NULL    = 0
	EMPTY   = 1
	LOAD    = 2
	SAVE    = 3
	QUIT    = 4
	INVALID = 5
	SET     = 6
	GET     = 7
	PRINT   = 8
	DELETE  = 9
	CLEAR   = 10

class eMoneySourceType(Enum):
	NULL = 0
	BANK = 1
	CASH = 2

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

