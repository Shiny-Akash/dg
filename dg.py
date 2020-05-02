'''dg - Dataset Generator'''
import os 
import cv2
import json
import shutil
import random
import numpy as np

class DataSetGenerator:
	"""
	this is the main class from which many
	subclasses are derived .
	"""
	def __init__(self,name):
		"""
		basic attributes and functions that
		has to initialized for every dataset
		class .
		"""
		self.name = name
		self.ids = []
		self.paths = []
		self.bgs = []

	def __getitem__(self,idx):
		return {'image_id': self.ids[idx],
				'path':self.paths[idx],
				'bg':self.bgs[idx]}
		
	def generate(self):
		"""call general functions for data generation"""
		self.make_path()
		self.create_list()
		self.create_json()

	def make_path(self):
		"""
		create default directories for storing the
		dataset csv file and the images .
		"""
		folders = [f'{self.name}/json/',f'{self.name}/images/']
		for folder in folders:
			if not os.path.exists(folder):
				os.makedirs(folder)

	def create_list(self):
		"""create image ids and paths .""" 
		for _ in range(self.count):
			id_ = random.randint(10000,99999)
			self.ids.append(id_)
			self.paths.append(
				f"{self.name}/images/{id_}.jpg")

	def create_json(self):
		"""create json file to store ids,paths and bgs"""
		data = {'image_id':self.ids,
				'path':self.paths,
				'bg':self.bgs}
		with open(f'{self.name}/json/images_info.json','w')as f:
			json.dump(data, f)

	def cleanup(self):
		"""delete already existing dataset"""
		if os.path.exists(f'{self.name}'):
			shutil.rmtree(f'{self.name}')

class PlainSet(DataSetGenerator):
	"""a plain images dataset generator"""
	def __init__(self,name,bg=None):
		super().__init__(name)
		self.bg = bg

	def generate(self,size,count,channels=3):
		"""
		generate images and return the list of 
		ids , paths ,etc (dataset obj)
		"""
		self.size = size
		self.count = count
		self.channels = channels
		super().generate()
		self.gen()

	def create_list(self):
		"""
		handle the backgrounds specific for 
		PlainSet .
		"""
		super().create_list()
		for _ in range(self.count):
			if not self.bg :
				bg = [random.randint(0,255) 
							for _ in range(self.channels)]
			elif len(self.bg) != 1 :
				bg = random.sample(self.bg,1)
			else :
				bg = self.bg 
			self.bgs.append(bg)

	def gen(self):
			"""the actual image generator"""
			(h,w),c = self.size,self.channels
			for path,bg in zip(self.paths,self.bgs):
				plain = np.ones((h,w,c),dtype=np.uint8)
				plain = plain*bg
				cv2.imwrite(path,plain)

class ObjectSet(DataSetGenerator):
	"""
	common class for both object over plainset 
	and object over some backgrounds
	"""
	def __init__(self,name,obj,bg=None):
		"""get the object image"""
		#add bg to the arguement bcoz of mro
		super().__init__(name,bg=bg)
		self.object = obj

class ObjectOverPlainSet(ObjectSet,PlainSet):
	"""object over plain images ."""
	#so inherited both objectset and plainset .  
	def __init__(self,name,obj,bg=None):
		"""
		get the object as well as colour of 
		the plain image if given
		"""
		super().__init__(name,obj,bg=bg)


ob = ObjectOverPlainSet("dataset",'object')
ob.cleanup()
ob.generate((500,500),10)