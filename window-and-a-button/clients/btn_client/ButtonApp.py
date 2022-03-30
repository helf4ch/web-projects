from ButtonFrame import ButtonFrame
from tkinter import Tk 


class ButtonApp(Tk):
    
    def __init__(self, func):
        super().__init__()
        self.title("Button App")
        self.initUI(func)
        
    
    def initUI(self, func):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        button = ButtonFrame(self, func)
        button.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)


def main():
    buttonApp = ButtonApp(main)
    buttonApp.mainloop()


if __name__ == "__main__":
    main()
        