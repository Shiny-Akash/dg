'''dg - Dataset Generator'''
import os 

class DataSetGenerator:
	def __init__(self):
		self.make_path()
		
	def make_path(self):
		folders = ['dataset/csv/','dataset/images/']
		for folder in folders:
			if not os.path.exists(folder):
				os.makedirs(folder)

class PlainSet(DataSetGenerator):
	def __init__(self,count,bg=None):
		self.count = count
		self.bg = bg
		super().__init__()

if __name__ == "__main__":
	plain = PlainSet(10)