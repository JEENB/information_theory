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

	def kraft_inequality(self) -> bool:
		'''
		Checks whether krafts inequality is satisfied or not
		'''
		D = len(self.d)
		sumation = 0
		for p in self.prob:
			sumation += D^math.ceil(math.log2(p))
		if sumation < 1:
			return True
		else:
			return False

	def shanon_fano_code(self):
		'''
		Gives the shano fano encoding for as source as per the binary tree. 

		TODO: Implement this part
		'''
		pass

	def huffman_code(self):
		'''
		Give the huffman encoding for a source with a probability distn

		TODO: Implement this part
		'''
	
	def shanon_fano_elias_code(self):
		'''
		Gives the shanon fano elias encoding for the source

		TODO: Implement this part
		
		'''

class MultiDistributionInfomation:

	'''TODO: This part can be implemented in a better way'''

	def __init__(self, dist_data: list) -> None:
		'''Takes the data class as input (list)'''

		if len(dist_data) < 2:
			raise exceptions.MultiDistnError(f"Excected 2 distributions got {len(dist_data)}")

		self.multi_dist = list()

		for i, dist in enumerate(dist_data):
			if not isinstance(dist, Data):
				raise exceptions.InstanceError(f"Data at index {i} not instance of data class")

			self.multi_dist.append(dist)

	def relative_entropy(self, index:list) -> float:
		'''
		for a range of distribution takes a two disribution and computes the relative entropy between the two distributions

		eg:d = MultiDistributionInfomation(a, b, c, d, e, f)
		d.relative_entropy(index = [1,2])
		computes relative distribution between b and c

		Note: For the two distributions the symbols should match to get the relative entropy
		We consider the distribution at index[1] to be the TRUE distribution and the second to be the estimated distribution
		'''
		if len(index) != 2:
			raise exceptions.LengthMismatch(f"Excpected 2 distribution but got {len(index)} distribution")
		
		for d in index:
			if not isinstance(d, int):
				raise exceptions.TypeError(f"Excepted int got {type(d)}")
		x = self.multi_dist[index[0]]
		y = self.multi_dist[index[1]]

		true_dist = dict(zip(x.symbols,x.prob))
		estimated_dist = dict(zip(y.symbols,y.prob))

		if sorted(true_dist.keys()) != sorted(estimated_dist.keys()):
			raise exceptions.SymbolsMismatch("Source Symbols are different")

		self.rel_entropy = 0

		for k in true_dist.keys():
			self.rel_entropy += true_dist[k] * math.log2(true_dist[k]/ estimated_dist[k])

		return self.rel_entropy
		

		




d1 = Data(['a', 'b'], [0.5, 0.5])
d2 = Data(['a', 'b'], [0.75, 0.25])

f = MultiDistributionInfomation(dist_data = [d1, d2])
print(f.relative_entropy(index=[0,1]))