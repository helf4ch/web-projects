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
        self.initUI()
        self.title("Setup")


    def initUI(self):
        self.columnconfigure(0, weight=1, minsize=400)
        self.rowconfigure(0, weight=1, minsize=60)

        self.btn_fr = Frame(self)

        for i in range(0, 3):
            self.btn_fr.rowconfigure(i, weight=1)

        self.btn_fr.columnconfigure(0, weight=1)

        self.btn_fr.grid(row=0, column=0, sticky='nsew')

        self.top_btn = OpenFileButton(self.btn_fr, 'First image')
        self.mid_btn = OpenFileButton(self.btn_fr, 'Second image')
        self.btm_btn = Button(self.btn_fr, text='OK', command=self.close)

        self.top_btn.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.mid_btn.grid(row=1, column=0, sticky='nsew', padx=5)
        self.btm_btn.grid(row=2, column=0, sticky='nsew', padx=5, pady=5)


    def close(self):
        if not self.top_btn.filepath and not self.mid_btn.filepath:
            messagebox.showerror("ERROR", "Images doesn't set")
            return
        elif not self.top_btn.filepath: 
            messagebox.showerror("ERROR", "First image doesn't set")
            return
        elif not self.mid_btn.filepath:
            messagebox.showerror("ERROR", "Second image doesn't set")
            return

        self.destroy()


def main():
    test = SetupWindow()
    test.mainloop()


if __name__ == '__main__':
    main()

