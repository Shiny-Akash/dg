from gui import BaseApp
import dg

class DGapp(BaseApp):
	def __init__(self):
		super().__init__(generate_button_callback=self.generate,
						clean_button_callback=self.clean,
						)

	def generate(self):
		self.dataset = self.get_dg(self.d_var.get())
		count = int(self.count_entry.get())
		size = int(self.sizex_entry.get()),int(self.sizey_entry.get())
		self.dataset.cleanup()
		self.dataset.generate(count=count, size=size)
		print('done')

	def get_dg(self,t):
		datasets = {
				'PlainSet':dg.PlainSet,
				'ObjectOverPlainSet':dg.ObjectOverPlainSet,
				'ObjectOverBackgroundSet':dg.ObjectOverBackgroundSet,
				}
		d = datasets.get(t)
		name = self.name_entry.get()
		return d(name=name)

	def clean(self):
		self.dataset = self.get_dg(self.d_var.get())
		self.dataset.cleanup()

if __name__ == '__main__':
	app = DGapp()
	app.run()