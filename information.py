from logging import exception
from data import *
import exceptions

class Information(Data):

	def __init__(self, symbols: list, prob: list):
		super().__init__(symbols, prob)
		self.entropy = None

	def shanon_entropy(self, show_steps = False) -> float:
		''' 
		Computes the shanon entroy as sum(p(x)log(p(x)))

		TODO: Implement show steps
		'''
		entropy = 0
		
		for p in self.prob:
			entropy += p*math.log2(p)
		self.entropy = (-1) * entropy

		
		if show_steps:
			print("H(X) = ", end = '')
			for i, p in enumerate(self.prob):
				if i != len(self.prob):
					print(f"{p}log2({p})", end=' + ')
				else:
					print(end='=')
		return self.entropy

	def shanon_fano_code(self):
		'''
		Gives the shano fano encoding for as source as per the binary tree. 

		TODO: Implement this part
		'''
		pass


class MultiDistributionInfomation:

	def __init__(self, dist_data: list) -> None:
		'''Takes the data class as input (list)'''

		if len(dist_data) < 2:
			raise exceptions.MultiDistnError("Excected atlest 2 distribution")

		self.multi_dist = list()

		for i, dist in enumerate(dist_data):
			if not isinstance(dist, Data):
				raise exceptions.InstanceError(f"Data at index {i} not instance of data class")
			self.multi_dist.append(dist)

	def relative_entropy(self, index:list):
		'''
		for a range of distribution takes a two disribution and computes the relative entropy between the two distributions

		eg:d = MultiDistributionInfomation(a, b, c, d, e, f)
		d.relative_entropy(index = [1,2])
		computes relative distribution between b and c
		'''
		if len(index) != 2:
			raise exceptions.LengthMismatch(f"Excpected 2 distribution but got {len(index)} distribution")
		
		for d in index:
			if not isinstance(d, int):
				raise exceptions.TypeError(f"Excepted int got {type(d)}")
		x = self.multi_dist[index[0]]
		y = self.multi_dist[index[1]]
	
d = Data(['a', 'b'], [0.5, 0.5])
inf = Information(['a', 'b'], [0.5, 0.5])
print(inf.shanon_entropy(show_steps=True))