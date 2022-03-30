from tkinter import Frame, Canvas
from PIL import Image, ImageTk

class Image_frame(Frame):

    def __init__(self, parent, img_path1, img_path2):
        super().__init__(parent)
        self.parent = parent
       
        self.img_path1 = img_path1
        self.img_path2 = img_path2

        self.open_img(self.img_path1)

    def open_img(self, path):
        self.img = Image.open(path)
        self.photo = ImageTk.PhotoImage(self.img)
        self.canvas = Canvas(self, height=self.img.size[1]+20, width=self.img.size[0]+20)
        self.canvas.create_image(10, 10, anchor='nw', image=self.photo)
        self.canvas.grid(row=0, column=0)
        self.cur_path = path

    def change_img(self):
        if self.cur_path == self.img_path1:
            self.cur_path = self.img_path2
        else:
            self.cur_path = self.img_path1

        self.open_img(self.cur_path)


def main():
    # Test
    from tkinter import Tk
    window = Tk()
    img_fr = Image_frame(window, "img1.png", "img2.png")
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    img_fr.grid(row=0, column=0)
    #img_fr.change_img()
    window.mainloop()

if __name__ == '__main__':
    main()

