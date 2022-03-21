import img_frame
import setup_window
import tkinter

stp_wndw = setup_window.Setup_window()
stp_wndw.mainloop()
window = tkinter.Tk()
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
print(stp_wndw.top_btn.filepath)
print(stp_wndw.mid_btn.filepath)
img_frm = img_frame.Image_frame(window, f"{stp_wndw.top_btn.filepath}", f"{stp_wndw.mid_btn.filepath}")
img_frm.grid(row=0, column=0, padx=5, pady=5)
btn = tkinter.Button(window, text="press me", command=img_frm.change_img)
btn.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
window.mainloop()

