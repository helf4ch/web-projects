from tkinter import *
from PIL import ImageTk, Image
#window options
window = Tk()
window.title('picture viewer(v0.04alpha)')
window.geometry('800x600')
window['bg'] = 'grey'

for i in range(3):
        window.columnconfigure(i, weight=1, minsize=70)
        window.rowconfigure(i, weight=1, minsize=70)
#img
pil_image = Image.open("img1.png")


image = ImageTk.PhotoImage(pil_image)
canvas = Canvas(window, width=pil_image.size[0], height=pil_image.size[1])

image_sprite = canvas.create_image(2, 2, anchor='nw', image=image)
canvas.grid(row=1, column=1)

label_pic_name = Label(window, text='<< image_test2.jpg >>')                           
label_pic_name.grid(row=2, column=1)                            

#bottons_top
frame_top = Frame(window, width=100, height=100)
frame_top.grid(row=0, column=1)
btn1 = Button(frame_top, text="1111",        
                     background="#555",  
                                  foreground="#ccc",     
                                               activebackground='#557',
                                                            font="16",
                                                                         padx=5
                                                                                      )
btn1.grid(row=0, column=1)

btn2 = Button(frame_top, text="2222",        
                     background="#555",  
                                  foreground="#ccc",     
                                               activebackground='#557',
                                                            font="16",            
                                                                         )
btn2.grid(row=0, column=2)

btn3 = Button(frame_top, text="3333",        
                     background="#555",  
                                  foreground="#ccc",     
                                               activebackground='#557',
                                                            font="16",
                                                                         padx=5
                                                                                      )
btn3.grid(row=0, column=3)

btn4 = Button(frame_top, text="4444",        
                     background="#555",  
                                  foreground="#ccc",     
                                               activebackground='#557',
                                                            font="16",
                                                                         padx=5
                                                                                      )
btn4.grid(row=0, column=4)

#bottons_side
frame_side = Frame(window)
frame_side.grid(row=1, column=0, padx=10)
btn11 = Button(frame_side, text="1111",        
                     background="#555",  
                                  foreground="#ccc",     
                                               activebackground='#557',
                                                            font="16",
                                                                        
                                                                         )
btn11.grid(row=1, column=0)

btn22 = Button(frame_side, text="2222",        
                     background="#555",  
                                  foreground="#ccc",     
                                               activebackground='#557',
                                                            font="16",
                                                                        
                                                                         )
btn22.grid(row=2, column=0)

btn33 = Button(frame_side, text="3333",        
                     background="#555",  
                                  foreground="#ccc",     
                                               activebackground='#557',
                                                            font="16",
                                                                         
                                                                         )
btn33.grid(row=3, column=0)

btn44 = Button(frame_side, text="4444",        
                     background="#555",  
                                  foreground="#ccc",     
                                               activebackground='#557',
                                                            font="16",
                                                                        
                                                                         )
btn44.grid(row=4, column=0)
window.mainloop()
