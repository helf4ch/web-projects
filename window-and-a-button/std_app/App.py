from SetupWindow import SetupWindow
from ImageFrame import ImageFrame
from ButtonFrame import ButtonFrame
from tkinter import Tk


class App(Tk):
    
    def __init__(self, filepaths):
        super().__init__()
        self.title("App")
        self.initUI(filepaths)
        
    
    def initUI(self, filepaths):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        
        imageFrame = ImageFrame(self, filepaths[0], filepaths[1])
        imageFrame.grid(row=0, column=0, padx=5, pady=5)
        
        button = ButtonFrame(self, imageFrame.changeImage)
        button.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        
        
def main():
    setupWindow = SetupWindow()
    setupWindow.mainloop()
    app = App(setupWindow.getImagesPaths())
    app.mainloop()
    

if __name__ == "__main__":
    main()
 