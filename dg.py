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
		
	def generate(self,size,count,
				channels=3):
		"""call general functions for data generation"""
		self.h,self.w = size
		self.count = count
		self.channels = channels
		self.make_path()
		self.create_list()
		self.create_json()
		for path,img,mask in self.gen():
			cv2.imwrite(path,img)
			if mask.any() :
				*p,id_=path.split('/')
				cv2.imwrite(f"{self.name}/masks/{id_}",
							mask)

	def make_path(self):
		"""
		create default directories for storing the
		dataset csv file and the images .
		"""
		folders = [f'{self.name}/json/',
					f'{self.name}/images/']
		if hasattr(self,'masks'):
			folders.append(f'{self.name}/masks/')
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
			if hasattr(self,'masks'):
				self.masks.append(
				f"{self.name}/masks/{id_}.png")

	def create_json(self):
		"""create json file to store ids,paths and bgs"""
		data = {'image_id':self.ids,
				'img_path':self.img_paths,
				'bg':self.bgs}
		if hasattr(self,'bbox'):
			data['masks'] = self.masks
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

	def gen(self):
			"""generate images and return path ,img"""
			c = self.channels
			for path,bg in zip(self.img_paths,self.bgs):
				plain = np.ones((self.h,self.w,c),
								dtype=np.uint8)
				yield path,(plain*bg).astype(np.uint8),None

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
		obj = cv2.imread(obj,-1)
		self.object = obj
		if obj.shape[2] == 4 :
			self.alpha = obj[:,:,3]
		else :
			self.alpha = np.ones(obj.shape[:2],
						dtype=np.uint8)*255
		self.bbox = []
		self.masks = []

	def create_bbox(self):
		"""create bbox list"""
		h,w,c = self.object.shape
		for _ in range(self.count):
			x = random.randrange(0,self.w-w)
			y = random.randrange(0,self.h-h)
			self.bbox.append([x,y,w,h])

	def alpha_blend(self,img,bbox):
		"""do alpha blending"""
		x,y,w,h = bbox
		for i in range(0,3):
			img[y:y+h,x:x+w,i] = (img[y:y+h,x:x+w,i]
								* (1-self.alpha/255.0)
								+ self.object[:,:,i]
								* (self.alpha/255.0))
		mask = np.zeros((self.h,self.w),dtype=np.uint8)
		mask[y:y+h,x:x+w] = self.alpha/255
		return img,mask


class ObjectOverPlainSet(ObjectSet,PlainSet):
	"""object over plain images ."""
	#so inherited both objectset and plainset

	def create_list(self):
		super().create_list()
		self.create_bbox()

	def gen(self):
		"""
		call plainimage generator and return 
		the alpha blended image
		"""
		for bbox,(path,plain,_) in zip(self.bbox,
								super().gen()):
			plain,mask = self.alpha_blend(plain,bbox)
			yield path,plain,mask


ob = ObjectOverPlainSet("dataset",'cursor.png',
						[(0,0,255),(0,255,255)])
ob.cleanup()
ob.generate((1000,1000),10)