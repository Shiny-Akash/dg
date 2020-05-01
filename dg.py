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
	def __init__(self):
		"""
		basic attributes and functions that
		has to initialized for every dataset
		class .
		"""
		self.ids = []
		self.paths = []
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
		folders = ['dataset/json/','dataset/images/']
		for folder in folders:
			if not os.path.exists(folder):
				os.makedirs(folder)

	def create_list(self):
		"""create image ids ,paths and backgrounds""" 
		for i in range(self.count):
			id_ = random.randint(10000,99999)
			self.ids.append(id_)
			self.paths.append(
				f"dataset/images/{id_}.jpg")
			rand_colour = [random.randint(0,255) 
							for _ in range(3)]
			self.bgs.append(rand_colour)

	def create_json(self):
		"""create json file to store ids,paths and bgs"""
		data = {'image_id':self.ids,
				'paths':self.paths,
				'bgs':self.bgs}
		with open('dataset/json/images_info.json','w')as f:
			json.dump(data, f)

	def cleanup(self):
		"""delete already existing dataset"""
		if os.path.exists('dataset'):
			shutil.rmtree('dataset')

class PlainSet(DataSetGenerator):
	"""a plain images dataset generator"""
	def __init__(self,bg=None):
		self.bg = bg
		super().__init__()

	def generate(self,size,count,channels=3):
		"""
		generate images and return the list of 
		ids , paths ,etc (dataset obj)
		"""
		self.size = size
		self.count = count
		self.channels = channels
		super().generate()
		for path,bg in zip(self.paths,self.bgs):
			img = self.gen(bg)
			cv2.imwrite(path,img)

	def gen(self,bg):
			"""the actual image generator"""
			(h,w),c = self.size,self.channels
			plain = np.ones((h,w,c),dtype=np.uint8)
			
			plain = plain*bg
			return plain

plain = PlainSet()
plain.cleanup()
plain.generate(size=(200,200) ,count=1)