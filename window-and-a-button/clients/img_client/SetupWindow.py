from tkinter import Tk, Button, Frame, messagebox
from tkinter.filedialog import askopenfilename


class OpenFileButton(Button):
    
    def __init__(self, parent, text):
        super().__init__(parent, text=text, command=self.openFile)
        self.filepath = None


    def openFile(self):
        self.filepath = askopenfilename()

        if not self.filepath:
            return

        self["text"] = f"{self.filepath}"


class SetupWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("Setup")
        self.initUI()


    def initUI(self):
        self.columnconfigure(0, weight=1, minsize=400)
        self.rowconfigure(0, weight=1, minsize=60)

        self.buttonFrame = Frame(self)

        for i in range(0, 3):
            self.buttonFrame.rowconfigure(i, weight=1)

        self.buttonFrame.columnconfigure(0, weight=1)

        self.buttonFrame.grid(row=0, column=0, sticky='nsew')

        self.topButton = OpenFileButton(self.buttonFrame, 'First image')
        self.midButton = OpenFileButton(self.buttonFrame, 'Second image')
        self.bottomButton = Button(self.buttonFrame, text='OK', command=self.close)

        self.topButton.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.midButton.grid(row=1, column=0, sticky='nsew', padx=5)
        self.bottomButton.grid(row=2, column=0, sticky='nsew', padx=5, pady=5)


    def close(self):
        if not self.topButton.filepath and not self.midButton.filepath:
            messagebox.showerror("ERROR", "Images doesn't set")
            return
        elif not self.topButton.filepath: 
            messagebox.showerror("ERROR", "First image doesn't set")
            return
        elif not self.midButton.filepath:
            messagebox.showerror("ERROR", "Second image doesn't set")
            return

        self.destroy()
        
    
    def getImagesPaths(self):
        return (f"{self.topButton.filepath}", f"{self.midButton.filepath}")


def main():
    # Test
    test = SetupWindow()
    test.mainloop()


if __name__ == '__main__':
    main()

