from ImageFrame import ImageFrame
from SetupWindow import SetupWindow
from tkinter import Tk


class ImageApp(Tk):
    
    def __init__(self, filepaths):
        super().__init__()
        self.title("Image App")
        self.initUI(filepaths)
        
    def initUI(self, filepaths):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        imageFrame = ImageFrame(self, filepaths[0], filepaths[1])
        imageFrame.grid(row=0, column=0, padx=5, pady=5)
        

def main():
    setupWindow = SetupWindow()
    setupWindow.mainloop()
    imageApp = ImageApp(setupWindow.getImagesPaths())
    imageApp.mainloop()
    
    
if __name__ == "__main__":
    main()
