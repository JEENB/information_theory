import math
import exceptions


class Data:
	'''
	data takes symbols and the associated probabilities as a list
	eg: 
	symbols = ['a', 'b', 'c']
	prob = [0.5, 0.25, 0.25]
	
	'''

	def __init__(self, symbols: list, prob: list, d = [0,1]):
		self.symbols 	= symbols
		self.prob 		= prob
		self.d 			= d

		if len(self.symbols) != len(set(self.symbols)):
			raise(exceptions.Duplicate(f"Duplicate Symbols detected"))

		if len(self.symbols) != len(self.prob):
			raise(exceptions.SrcDataMismatch(f"Symbol and probability length mismatch \nExpected {max(self.symbols, self.prob)} got {min(self.symbols, self.prob)}"))

		for p in self.prob:
			if isinstance(p, float):
				pass
			else: 
				raise(exceptions.TypeError(f"Expected float got {type(p)}"))
		
		if sum(self.prob) != 1:
			print("here")
			raise(exceptions.ProbabilityMismatch(f"Probabilities don't add to 1, got {sum(self.prob)}"))			



