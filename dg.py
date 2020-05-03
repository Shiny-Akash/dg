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
		self.img_paths = []
		self.bgs = []
		
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
			self.img_paths.append(
				f"{self.name}/images/{id_}.png")

	def create_json(self):
		"""create json file to store ids,paths and bgs"""
		data = {'image_id':self.ids,
				'img_path':self.img_paths,
				'bg':self.bgs}
		if hasattr(self,'bbox'):
			data['bbox'] = self.bbox
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
		self.h,self.w = size
		self.count = count
		self.channels = channels
		super().generate()
		for path,img in self.gen():
			cv2.imwrite(path,img)

	def gen(self):
			"""generate images and return path ,img"""
			c = self.channels
			for path,bg in zip(self.img_paths,self.bgs):
				plain = np.ones((self.h,self.w,c),
								dtype=np.uint8)
				yield path,(plain*bg).astype(np.uint8)

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


class ObjectSet(DataSetGenerator):
	"""
	common class for both object over plainset 
	and object over some backgrounds
	"""
	def __init__(self,name,obj,bg=None):
		"""get the object image"""
		#add bg to the arguement bcoz of mro
		super().__init__(name,bg=bg)
		obj = cv2.imread(obj)
		self.object = obj
		self.bbox = []

	def create_list(self):
		"""
		add bbox attribute to the list 
		"""
		super().create_list()
		h,w,c = self.object.shape
		for _ in range(self.count):
			x = random.randrange(0,self.w-w)
			y = random.randrange(0,self.h-h)
			self.bbox.append([x,y,w,h])


class ObjectOverPlainSet(ObjectSet,PlainSet):
	"""object over plain images ."""
	#so inherited both objectset and plainset .  
	def __init__(self,name,obj,bg=None):
		"""
		get the object as well as colour of 
		the plain image if given
		"""
		super().__init__(name,obj,bg=bg)

	def gen(self):
		for (x,y,w,h),(path,plain) in zip(self.bbox,
									super().gen()):
			plain[x:x+w,y:y+h] = self.object
			plain = cv2.cvtColor(plain,cv2.COLOR_RGB2RGBA)
			mask = np.zeros((self.h,self.w),
							dtype=np.uint8)
			mask[x:x+w,y:y+h] = 255
			plain[:,:,3] = mask
			yield path,plain


ob = ObjectOverPlainSet("dataset",'skystone.png',
						[(0,0,0),(255,255,255)])
ob.cleanup()
ob.generate((1000,1000),10)

img =  cv2.imread(ob.img_paths[0],-1)
print(img.shape)