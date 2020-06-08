from gui import BaseApp
import dg

class DGapp(BaseApp):
	def __init__(self):
		super().__init__(self.generate)

	def generate(self):
		self.dataset = self.get_dg(self.d_var.get())

	def get_dg(self,t):
		datasets = {
				'PlainSet':dg.PlainSet,
				'ObjectOverPlainSet':dg.ObjectOverPlainSet,
				'ObjectOverBackgroundSet':dg.ObjectOverBackgroundSet,
				}
		return datasets.get(t)

if __name__ == '__main__':
	app = DGapp()
	app.run()