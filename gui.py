#!/usr/bin/env python3

"""build a basic gui for the app"""

import tkinter as tk


class BaseApp:
    def __init__(
        self, generate_button_callback=None, clean_button_callback=None,
    ):
        self.generate_callback = generate_button_callback
        self.clean_callback = clean_button_callback
        self.define_main_window()
        self.define_frames()
        self.frames_configuration()
        self.define_widgets()
        self.initial_packing()

    def define_main_window(self):
        self.window = tk.Tk()
        self.window.title("DataSetGenerator")
        self.window.minsize(600, 600)
        self.window.rowconfigure(0, weight=1)  # header row
        self.window.rowconfigure(1, weight=4)  # content row
        self.window.columnconfigure(0, weight=1)

    def define_frames(self):
        self.title_frame = tk.Frame(master=self.window, bg="red",)
        self.content_frame = tk.Frame(master=self.window, bg="green",)
        self.next_frame = tk.Frame(master=self.window, bg="green",)
        self.final_frame = tk.Frame(master=self.window, bg="green",)

    def frames_configuration(self):
        # title frame
        self.title_frame.rowconfigure(0, weight=1)
        self.title_frame.columnconfigure(0, weight=1)

        # content frame
        num_rows = 6
        for i in range(0, num_rows):
            self.content_frame.rowconfigure(i, weight=1)
        num_columns = 2
        for i in range(0, num_columns):
            self.content_frame.columnconfigure(i, weight=1)

        # next frame
        num_rows = 6
        for i in range(0, num_rows):
            self.next_frame.rowconfigure(i, weight=1)
        num_columns = 2
        for i in range(0, num_columns):
            self.next_frame.columnconfigure(i, weight=1)

        # final frame
        num_rows = 1
        for i in range(0, num_rows):
            self.final_frame.rowconfigure(i, weight=1)
        num_columns = 1
        for i in range(0, num_columns):
            self.final_frame.columnconfigure(i, weight=1)

    def define_widgets(self):

        # widgets in title frame
        self.title_lbl = tk.Label(
            master=self.title_frame,
            text="DataSet Generator",
            bg="red",
            fg="white",
            height=3,
            width=20,
            font=10,
        )

        # widgets in content frame
        self.typeofdataset_lbl = tk.Label(
            master=self.content_frame,
            text="Type of dataset :",
            bd=5,
            font=10,
            relief=tk.GROOVE,
        )
        # drop down menu
        dataset_list = ["PlainSet", "ObjectOverPlainSet", "ObjectOverBackgroundSet"]
        self.d_var = tk.StringVar(self.content_frame)
        self.d_var.set(dataset_list[0])
        self.typeofdataset_opt = tk.OptionMenu(
            self.content_frame, self.d_var, *dataset_list,
        )
        self.typeofdataset_opt.configure(font=10)

        self.name_lbl = tk.Label(
            master=self.content_frame,
            text="Name of the dataset :",
            bd=5,
            font=10,
            relief=tk.GROOVE,
        )
        self.name_entry = tk.Entry(
            master=self.content_frame, relief=tk.RIDGE, bd=5, font=10,
        )
        self.count_lbl = tk.Label(
            master=self.content_frame, text="Count :", bd=5, font=10, relief=tk.GROOVE,
        )
        self.count_entry = tk.Entry(
            master=self.content_frame, relief=tk.RIDGE, bd=5, font=10,
        )
        self.sizex_lbl = tk.Label(
            master=self.content_frame, text="size X :", bd=5, font=10, relief=tk.GROOVE,
        )
        self.sizex_entry = tk.Entry(
            master=self.content_frame, relief=tk.RIDGE, bd=5, font=10,
        )
        self.sizey_lbl = tk.Label(
            master=self.content_frame, text="size Y :", bd=5, font=10, relief=tk.GROOVE,
        )
        self.sizey_entry = tk.Entry(
            master=self.content_frame, relief=tk.RIDGE, bd=5, font=10,
        )
        self.next_button = tk.Button(
            master=self.content_frame,
            text="Next",
            fg="red",
            relief=tk.GROOVE,
            bd=10,
            font=10,
            command=self.next,
        )
        # widgets in next frame
        self.generate_button = tk.Button(
            master=self.next_frame,
            text="Generate",
            fg="red",
            relief=tk.GROOVE,
            bd=10,
            font=10,
            command=self.generate_callback,
        )
        self.clean_button = tk.Button(
            master=self.next_frame,
            text="Clean",
            fg="red",
            relief=tk.GROOVE,
            bd=10,
            font=10,
            command=self.clean_callback,
        )
        self.back_button = tk.Button(
            master=self.next_frame,
            text="Back",
            fg="red",
            relief=tk.GROOVE,
            bd=10,
            font=10,
            command=self.back,
        )
        self.savepath_lbl = tk.Label(
            master=self.next_frame, text="Save Path :", bd=5, font=10, relief=tk.GROOVE,
        )
        self.savepath_entry = tk.Entry(
            master=self.next_frame, relief=tk.RIDGE, bd=5, font=10,
        )
        self.bg_lbl = tk.Label(
            master=self.next_frame,
            text="Background :",
            bd=5,
            font=10,
            relief=tk.GROOVE,
        )
        self.bg_entry = tk.Entry(
            master=self.next_frame, relief=tk.RIDGE, bd=5, font=10,
        )
        self.obj_lbl = tk.Label(
            master=self.next_frame,
            text="Object Image :",
            bd=5,
            font=10,
            relief=tk.GROOVE,
        )
        self.obj_entry = tk.Entry(
            master=self.next_frame, relief=tk.RIDGE, bd=5, font=10,
        )
        self.resize_lbl = tk.Label(
            master=self.next_frame,
            text="Object Resize :",
            bd=5,
            font=10,
            relief=tk.GROOVE,
        )
        self.resize_entry = tk.Entry(
            master=self.next_frame, relief=tk.RIDGE, bd=5, font=10,
        )
        # final frame
        self.t_var = tk.StringVar()
        self.t_var.set("Generating......")
        self.generating_lbl = tk.Label(
            master=self.final_frame,
            textvariable=self.t_var,
            bd=10,
            font=10,
            bg="yellow",
            fg="red",
        )

    def initial_packing(self):
        # title frame
        self.title_frame.grid(row=0, sticky="nsew")
        self.title_lbl.grid()

        # content frame
        self.pack_content_frame()

    def pack_content_frame(self):
        self.content_frame.grid(row=1, sticky="nsew")

        self.typeofdataset_lbl.grid(row=0, column=0, sticky="e")
        self.typeofdataset_opt.grid(row=0, column=1, sticky="w", padx=10)
        self.name_lbl.grid(row=1, column=0, sticky="e")
        self.name_entry.grid(row=1, column=1, sticky="w", padx=10)
        self.count_lbl.grid(row=2, column=0, sticky="e")
        self.count_entry.grid(row=2, column=1, sticky="w", padx=10)
        self.sizex_lbl.grid(row=3, column=0, sticky="e")
        self.sizex_entry.grid(row=3, column=1, sticky="w", padx=10)
        self.sizey_lbl.grid(row=4, column=0, sticky="e")
        self.sizey_entry.grid(row=4, column=1, sticky="w", padx=10)
        self.next_button.grid(row=5, column=1, sticky="w", padx=10)

    def pack_next_frame(self):
        self.next_frame.grid(row=1, sticky="nsew")

        self.back_button.grid(row=0, column=0, padx=30)
        idx = -3
        if not self.d_var.get() == "PlainSet":
            idx = 0
            self.obj_lbl.grid(row=1, column=0, sticky="e")
            self.obj_entry.grid(row=1, column=1, sticky="w", padx=10)
            self.bg_lbl.grid(row=2, column=0, sticky="e")
            self.bg_entry.grid(row=2, column=1, sticky="w", padx=10)
            self.resize_lbl.grid(row=3, column=0, sticky="e")
            self.resize_entry.grid(row=3, column=1, sticky="w", padx=10)
        self.savepath_lbl.grid(row=idx + 4, column=0, sticky="e")
        self.savepath_entry.grid(row=idx + 4, column=1, sticky="w", padx=10)
        self.clean_button.grid(row=idx + 5, column=0, sticky="e")
        self.generate_button.grid(row=idx + 5, column=1, sticky="w", padx=50, pady=10)

    def pack_final_frame(self):
        self.final_frame.grid(row=1, sticky="nsew")
        self.generating_lbl.grid(row=0)

    def generate(self):
        self.next_frame.grid_forget()
        self.pack_final_frame()

    def next(self):
        self.content_frame.grid_forget()
        self.pack_next_frame()

    def back(self):
        self.next_frame.grid_forget()
        self.final_frame.grid_forget()
        self.pack_content_frame()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = BaseApp()
    app.run()
