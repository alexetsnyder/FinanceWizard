#FinWizExcept

from FinWizEnum import *

class FinWizError(Exception):
	"""Base class for exceptions in this project"""
	pass

class ParseError(FinWizError):
	"""Exeptions cause by Invalid command"""
	def __init__(self, message):
		self.message = message

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

class ExecError(FinWizError):
	"""Exceptions for the FinWizExec Module"""
	def __init__(self, message):
		self.message = message

class ArgumentError(ExecError):
	"""Exceptions for incorrect arguments"""
	def __init__(self, place, arg):
		self.message = 'Error: In ' + place + ': Bad Argument provided ' + arg 