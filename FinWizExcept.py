#FinWizExcept

from FinWizEnum import *

class FinWizError(Exception):
	"""Base class for exceptions in this project"""
	pass

class DataError(FinWizError):
	"""Base class for data exceptions in this project"""
	pass

class DateError(DataError):
	"""Exceptions caused by bad date input."""
	def __init__(self, place, datePart=eDate.NULL, message=eNull.STR):
		if datePart == eDate.YEAR:
			self.message = 'Error: In ' + place + ': Invalid Year...'
		elif datePart == eDate.MONTH:
			self.message = 'Error: In ' + place + ': Invalid Month...'
		elif datePart == eDate.DAY:
			self.message = 'Error: In ' + place + ': Invalid Day...'
		else:
			self.message = 'Error: In ' + place + ': ' +  message + '...'
