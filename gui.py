import tkinter as tk
if __name__ == '__main__':

	def generate():
		pass

	# main window 
	window = tk.Tk()
	window.title('DataSetGenerator')
	window.minsize(600,600)
	window.rowconfigure(0,weight=1)
	window.columnconfigure(0,weight=1)
	window.rowconfigure(1,weight=3)

	# frames
	title_frame = tk.Frame(
					master=window,
					bg='red',
					)
	content_frame = tk.Frame(
					master=window,
					bg='green',
					)

	# configuration
	title_frame.rowconfigure(0,weight=1)
	title_frame.columnconfigure(0,weight=1)

	nrows = 4 # number of rows
	for i in range(0,nrows):
		content_frame.rowconfigure(i,weight=1)
	ncolumns = 2 # number of columns
	for i in range(0,ncolumns):
		content_frame.columnconfigure(i,weight=1)

	# widgets
	title_lbl = tk.Label(
				master=title_frame,
				text='DataSet Generator',
				bg='red',
				fg='white',
				height=3,
				width=20,
				font=10,
				)
	typeofdataset_lbl = tk.Label(
						master=content_frame,
						text='Type of dataset :',
						bd=5,
						font=10,
						relief=tk.GROOVE)
	typeofdataset_entry = tk.Entry(
						master=content_frame,
						relief=tk.RIDGE,
						bd=5,
						font=10,
						)
	count_lbl = tk.Label(
						master=content_frame,
						text='Count :',
						bd=5,
						font=10,
						relief=tk.GROOVE,
						)
	count_entry = tk.Entry(
						master=content_frame,
						relief=tk.RIDGE,
						bd=5,
						font=10,
						)
	size_lbl = tk.Label(
						master=content_frame,
						text='size :',
						bd=5,
						font=10,
						relief=tk.GROOVE,
						)
	size_entry = tk.Entry(
						master=content_frame,
						relief=tk.RIDGE,
						bd=5,
						font=10,
						)
	generate_button = tk.Button(
						master=content_frame,
						text='Generate',
						fg='red',
						relief=tk.GROOVE,
						bd=10,
						font=10,
						command=generate)

	# packing
	title_frame.grid(row=0,sticky='nsew')
	title_lbl.grid()

	content_frame.grid(row=1,sticky='nsew')
	typeofdataset_lbl.grid(row=0,column=0,sticky='e')
	typeofdataset_entry.grid(row=0,column=1,sticky='w',padx=10)
	count_lbl.grid(row=1,column=0,sticky='e')
	count_entry.grid(row=1,column=1,sticky='w',padx=10)
	size_lbl.grid(row=2,column=0,sticky='e')
	size_entry.grid(row=2,column=1,sticky='w',padx=10)
	generate_button.grid(row=3,column=1,sticky='w',padx=50,pady=10)

	# mainloop
	window.mainloop()


class DGapp:
	def __init__(self,
				generate_button_callback=None,
				):
		self.generate = generate_button_callback
		self.main_window()
		self.frames()
		self.configuration()
		self.widgets()
		self.packing()
		self.run()

	def main_window(self):
		self.window = tk.Tk()
		self.window.title('DataSetGenerator')
		self.window.minsize(600,600)
		self.window.rowconfigure(0,weight=1)
		self.window.columnconfigure(0,weight=1)
		self.window.rowconfigure(1,weight=3)

	def frames(self):
		self.title_frame = tk.Frame(
					master=self.window,
					bg='red',
					)
		self.content_frame = tk.Frame(
					master=self.window,
					bg='green',
					)

	def configuration(self):
		self.title_frame.rowconfigure(0,weight=1)
		self.title_frame.columnconfigure(0,weight=1)

		nrows = 4 # number of rows
		for i in range(0,nrows):
			self.content_frame.rowconfigure(i,weight=1)
		ncolumns = 2 # number of columns
		for i in range(0,ncolumns):
			self.content_frame.columnconfigure(i,weight=1)

	def widgets(self):
		self.title_lbl = tk.Label(
					master=self.title_frame,
					text='DataSet Generator',
					bg='red',
					fg='white',
					height=3,
					width=20,
					font=10,
					)
		self.typeofdataset_lbl = tk.Label(
							master=self.content_frame,
							text='Type of dataset :',
							bd=5,
							font=10,
							relief=tk.GROOVE)
		self.typeofdataset_entry = tk.Entry(
							master=self.content_frame,
							relief=tk.RIDGE,
							bd=5,
							font=10,
							)
		self.count_lbl = tk.Label(
							master=self.content_frame,
							text='Count :',
							bd=5,
							font=10,
							relief=tk.GROOVE,
							)
		self.count_entry = tk.Entry(
							master=self.content_frame,
							relief=tk.RIDGE,
							bd=5,
							font=10,
							)
		self.size_lbl = tk.Label(
							master=self.content_frame,
							text='size :',
							bd=5,
							font=10,
							relief=tk.GROOVE,
							)
		self.size_entry = tk.Entry(
							master=self.content_frame,
							relief=tk.RIDGE,
							bd=5,
							font=10,
							)
		self.generate_button = tk.Button(
							master=self.content_frame,
							text='Generate',
							fg='red',
							relief=tk.GROOVE,
							bd=10,
							font=10,
							command=self.generate)

	def packing(self):
		self.title_frame.grid(row=0,sticky='nsew')
		self.title_lbl.grid()

		self.content_frame.grid(row=1,sticky='nsew')
		self.typeofdataset_lbl.grid(row=0,column=0,sticky='e')
		self.typeofdataset_entry.grid(row=0,column=1,sticky='w',padx=10)
		self.count_lbl.grid(row=1,column=0,sticky='e')
		self.count_entry.grid(row=1,column=1,sticky='w',padx=10)
		self.size_lbl.grid(row=2,column=0,sticky='e')
		self.size_entry.grid(row=2,column=1,sticky='w',padx=10)
		self.generate_button.grid(row=3,column=1,sticky='w',padx=50,pady=10)

	def run(self):
		self.window.mainloop()