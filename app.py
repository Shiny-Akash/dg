#!/usr/bin/env python3

"""integrate the dg script and gui"""

from gui import BaseApp
import dg
import time


class DGapp(BaseApp):
    def __init__(self):
        super().__init__(
            generate_button_callback=self.generate, clean_button_callback=self.clean,
        )

    def generate(self):
        super().generate()
        self.dataset = self.get_dg(self.d_var.get())
        count = self.count_entry.get()
        size = self.sizex_entry.get(), self.sizey_entry.get()
        if count and size:
            count = int(count)
            size = int(size[0]), int(size[1])
            self.dataset.cleanup()
            self.dataset.generate(count=count, size=size)
            self.t_var.set("Done")
            self.window.after(1000, self.back)
        else:
            self.back()
            return

    def get_dg(self, t):
        name = self.name_entry.get()
        save_path = self.savepath_entry.get()
        obj = self.obj_entry.get().split(",")
        bg = self.bg_entry.get().split(",")
        if bg == "":
            bg = None
        resize = self.resize_entry.get()
        if resize == "":
            resize = None
        else:
            resize.replace("(", "")
            resize = resize.split(",")
            resize = int(resize[0]), int(resize[1])
        if t == "PlainSet":
            return dg.PlainSet(name=name, save_path=save_path,)
        if t == "ObjectOverPlainSet":
            return dg.ObjectOverPlainSet(
                name=name, save_path=save_path, obj=obj, resize=resize,
            )
        if t == "ObjectOverBackgroundSet":
            return dg.ObjectOverBackgroundSet(
                name=name, save_path=save_path, obj=obj, bg=bg, resize=resize,
            )

    def clean(self):
        self.dataset = self.get_dg(self.d_var.get())
        self.dataset.cleanup()


if __name__ == "__main__":
    app = DGapp()
    app.run()
