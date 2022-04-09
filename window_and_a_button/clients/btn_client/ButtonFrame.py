from tkinter import Frame, Button


class ButtonFrame(Frame):

    def __init__(self, parent, func):
        super().__init__(parent)
        self.parent = parent

        self.initUI(func)

    def initUI(self, func):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1, minsize=400)
        self.button = Button(self, text="press me", command=func)
        self.button.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)


def main():
    # Test

    from tkinter import Tk

    window = Tk()
    button = ButtonFrame(window, window.quit)

    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    button.grid(row=0, column=0)

    window.mainloop()


if __name__ == "__main__":
    main()
