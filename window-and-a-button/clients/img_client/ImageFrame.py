from tkinter import Frame, Canvas
from PIL import Image, ImageTk


class ImageFrame(Frame):

    def __init__(self, parent, imagePath1, imagePath2):
        super().__init__(parent)
        self.parent = parent

        self.imagePath1 = imagePath1
        self.imagePath2 = imagePath2

        self.openImage(self.imagePath1)

    def openImage(self, path):
        self.image = Image.open(path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(self,
                             height=self.image.size[1] + 20,
                             width=self.image.size[0] + 20)
        self.canvas.create_image(10, 10, anchor='nw', image=self.photo)
        self.canvas.grid(row=0, column=0)
        self.currentPath = path

    def changeImage(self):
        if self.currentPath == self.imagePath1:
            self.currentPath = self.imagePath2
        else:
            self.currentPath = self.imagePath1

        self.openImage(self.currentPath)


def main():
    # Test

    from tkinter import Tk

    window = Tk()

    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    ImageFrame = ImageFrame(window, "img1.png", "img2.png")
    ImageFrame.grid(row=0, column=0)

    #ImageFrame.changeImage()

    window.mainloop()


if __name__ == '__main__':
    main()
