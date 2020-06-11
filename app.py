from gui import BaseApp
import dg

class DGapp(BaseApp):
	def __init__(self):
		super().__init__(generate_button_callback=self.generate,
						clean_button_callback=self.clean,
						)

	def generate(self):
		self.dataset = self.get_dg(self.d_var.get())
		count = self.count_entry.get()
		size = self.sizex_entry.get(),self.sizey_entry.get()
		if count and size :
			count = int(count)
			size = int(size[0]),int(size[1])
			self.dataset.cleanup()
			self.dataset.generate(count=count, size=size)
			print('done')
		else : 
			print('Please enter correct values')

	def get_dg(self,t):
		datasets = {
				'PlainSet':dg.PlainSet,
				'ObjectOverPlainSet':dg.ObjectOverPlainSet,
				'ObjectOverBackgroundSet':dg.ObjectOverBackgroundSet,
				}
		d = datasets.get(t)
		name = self.name_entry.get()
		save_path = self.savepath_entry.get()
		return d(name=name,save_path=save_path)

	def clean(self):
		self.dataset = self.get_dg(self.d_var.get())
		self.dataset.cleanup()

if __name__ == '__main__':
	app = DGapp()
	app.run()