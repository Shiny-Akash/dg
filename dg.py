'''dg - Dataset Generator'''
import os 

class DataSetGenerator :
	name = "Dataset"
	def __init__(self ,save_path) :
		self.save_path = save_path
		if not os.path.exists(self.save_path):
			os.makedir(self.save_path)

class PlainSet(DataSetGenerator):
	def __init__(self,save_path,count
				,bg=False,) :
		self.count = count
		self.bg = bg
		super().__init__(save_path)

	