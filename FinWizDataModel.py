#FinWizDataModel

from FinWizExcept import DateError
from FinWizEnum import eDateFormat, eDate, eMonth, ePlace, eNull
from FinWizData import *

class Expense:
	def __init__(self, date, name, cost, category, source):
		self._date = date
		self._name = name
		self._cost = float(cost)
		self._category = category
		self._source = source

	def __str__(self):
		return '| ' + str(self._date) + ' | ' + self._name + ' | ' + str(self._cost) + ' | ' + self._category + ' | ' + SOURCE_TO_STRING[self._source]  + ' |' 

	def __repr__(self):
		return 'Date: ' + str(self._date) + ' Name: ' + self._name + ' Cost: ' + str(self._cost) + ' Category: ' + self._category + ' Source: ' + SOURCE_TO_STRING[self._source] 

class Revenue:
	def __init__(self, date, source, amount):
		self._date = date
		self._amount = float(amount)
		self._category = 'Revenue'
		self._source = source

	def __str__(self):
		return '| ' + str(self._date) + ' | ' + SOURCE_TO_STRING[self._source]  +  ' | ' + str(self._amount) + ' | ' + self._category + ' |' 

	def __repr__(self):
		return 'Date: ' + str(self._date) + ' Source: ' + SOURCE_TO_STRING[self._source] + ' Amount: ' + str(self._amount) + ' Category: ' + self._category 

class Date:
	def __init__(self, dateStr):
		self._year = eNull.INT
		self._day = eNull.INT
		self._month = eMonth.NULL
		
		self.initialize(DATE_FORMAT, dateStr.strip())

	def initialize(self, dateFormat, dateStr):
		self._dateFormat = dateFormat

		symbol = self.check_date_str(dateStr)
		if symbol == eNull.STR:
			raise DateError('__init__', eDate.NULL, 'symbol returned NULL')

		self.fill_date_pos(DATE_LOOKUP_TABLE[dateFormat][ePlace.FIRST], dateStr.partition(symbol)[0])
		self.fill_date_pos(DATE_LOOKUP_TABLE[dateFormat][ePlace.SECOND], dateStr.partition(symbol)[2].partition(symbol)[0])
		self.fill_date_pos(DATE_LOOKUP_TABLE[dateFormat][ePlace.THIRD], dateStr.partition(symbol)[2].partition(symbol)[2])

		self.check_days_in_month()

	def __str__(self):
		if self._dateFormat == eDateFormat.BIG_ENDIAN:
			return self.format_digits(eDate.YEAR) + '/' + self.format_digits(eDate.MONTH) + '/' + self.format_digits(eDate.DAY)
		elif self._dateFormat == eDateFormat.MIDDLE_ENDIAN:
			return self.format_digits(eDate.MONTH) + '/' + self.format_digits(eDate.DAY) + '/' + self.format_digits(eDate.YEAR)
		elif self._dateFormat == eDateFormat.LITTLE_ENDIAN:
			return self.format_digits(eDate.DAY) + '/' + self.format_digits(eDate.MONTH) + '/' + self.format_digits(eDate.YEAR)

	def __repr__(self):
		if self._dateFormat == eDateFormat.BIG_ENDIAN:
			return 'Format: ' + str(self._dateFormat) + '\n(' + str(self._year) + '/' + str(MONTH_TO_INT[self._month]) + '/' + str(self._day) + ')'
		elif self._dateFormat == eDateFormat.MIDDLE_ENDIAN:
			return 'Format: ' + str(self._dateFormat) + '\n(' + str(MONTH_TO_INT[self._month]) + '/' + str(self._day) + '/' + str(self._year) + ')'
		elif self._dateFormat == eDateFormat.LITTLE_ENDIAN:
			return 'Format: ' + str(self._dateFormat) + '\n(' + str(self._day) + '/' + str(MONTH_TO_INT[self._month]) + '/' + str(self._year) + ')'

	def year(self, year=None):
		if year == None:
			return self._year
		self._year = year

	def month(self, month=None):
		if month == None:
			return MONTH_TO_INT[self._month]
		self._month = month

	def day(self, day=None):
		if day == None:
			return self._day
		self._day = day

	def check_date_str(self, dateStr):
		sym_count = 0
		symbol = eNull.STR
		for x in dateStr:
			if not x.isdigit():
				if symbol == eNull.STR:
					symbol = x
					sym_count += 1
				elif x == symbol:
					sym_count += 1
				else:
					return eNull.STR

		if sym_count > 2:
			raise DateError('check_date_str', eDate.NULL, 'Too many symbols in date...')

		return symbol

	def fill_date_pos(self, datePos, val):
		if datePos == eDate.YEAR:
			tmpYear = int(val)
			if len(val) > 4 or tmpYear < 0:
				raise DateError('fill_date_pos', eDate.YEAR)
			self._year = tmpYear		
		elif datePos == eDate.MONTH:
			tmpMonth = int(val)
			if len(val) > 2 or tmpMonth < 1 or tmpMonth > 12:
				raise DateError('fill_date_pos', eDate.MONTH)
			self._month = INT_TO_MONTH[tmpMonth]
		elif datePos == eDate.DAY:
			tmpDay = int(val)
			if len(val) > 2 or tmpDay < 1 or tmpDay > 31:
				raise DateError('fill_date_pos', eDate.DAY)
			self._day = tmpDay

	def check_days_in_month(self):
		max_days = DAYS_IN_MONTH[self._month]
		if self._month == eMonth.FEBRUARY:
			#Is it a leap year
			if (self._year % 4 == 0 and self._year % 100 != 0) or self._year % 400 == 0:
				max_days += 1
		elif self._month == eMonth.NULL:
			raise DateError('check_days_in_month', eDate.MONTH)

		if self._day > max_days:
			raise DateError('check_days_in_month', eDate.DAY)

	def format_digits(self, datePart):
		if datePart == eDate.YEAR:
			prefix = ''.join(['0' for x in range(4 - len(str(self._year)))])
			return prefix + str(self._year)
		elif datePart == eDate.MONTH:
			month_str = str(MONTH_TO_INT[self._month])
			if len(month_str) == 1:
				month_str = '0' + month_str
			return month_str
		elif datePart == eDate.DAY:
			day_str = str(self._day)
			if len(day_str) == 1:
				day_str = '0' + day_str
			return day_str
		else:
			raise DateError('print_digits', eDate.NULL, 'datePart should not be NULL...')


if __name__ == '__main__':
	import sys

	while True:
		print('Choose a date format')
		print('1) yyyy/mm/dd')
		print('2) mm/dd/yyyy')
		print('3) dd/mm/yyyy')
		print('4) Month Test')
		print('q) Quit')
		choice = input("Enter a choice: ")

		dateFormat = eDateFormat.NULL
		forDateStr = eNull.STR
		if choice == 'q':
			break
		elif choice == '1':
			dateFormat = eDateFormat.BIG_ENDIAN
			forDateStr = 'yyyy/mm/dd'
		elif choice == '2':
			dateFormat = eDateFormat.MIDDLE_ENDIAN
			forDateStr = 'mm/dd/yyyy'
		elif choice == '3':
			dateFormat = eDateFormat.LITTLE_ENDIAN
			forDateStr = 'dd/mm/yyyy'
		elif choice == '4':
			for i in range(1, 13):
				try:
					date = Date(eDateFormat.MIDDLE_ENDIAN, str(i) + '/32/2017')
				except DateError as dateError:
					print('Month:', i)
					print(dateError.message)
			continue
		else:
			print('Incrrect choice. Try again.')
			continue

		print('Format:', forDateStr)
		dateStr = input("Enter a date: ")
		try:
			date = Date(dateFormat, dateStr)
			print(date)
		except DateError as dateError:
			print(dateError.message)





