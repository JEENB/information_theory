class SrcDataMismatch(Exception):
	'''Length and source data mismatch'''
	pass

class TypeError(Exception):
	'''Datatype in a datastructure mismatch'''
	pass

class ProbabilityMismatch(Exception):
	'''Raised when probability is not equal to 1'''
	pass

class MultiDistnError(Exception):
	'''Raised when multiple distributions are not detected'''
	pass

class InstanceError(Exception):
	'''Raised when an object is not an instance'''
	pass

class LengthMismatch(Exception):
	'''Raised when the length is mismatched'''
	pass

class Duplicate(Exception):
	'''Raised when duplicates are detected in a list'''
	pass

class SymbolsMismatch(Exception):
	'''Raised when symbols are mismatched '''
	pass