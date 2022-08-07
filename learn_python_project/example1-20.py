import tkinter 

root = tkinter.Tk()
r = tkinter.StringVar()
r.set('1')
radio = tkinter.Radiobutton(root, variable=r, value='1', text='China')
radio.pack()
radio = tkinter.Radiobutton(root, variable=r, value='2', text='America')
radio.pack()
radio = tkinter.Radiobutton(root, variable=r, value='3', text='Japan')
radio.pack()
radio = tkinter.Radiobutton(root, variable=r, value='4', text='Canada')
radio.pack()
radio = tkinter.Radiobutton(root, variable=r, value='5', text='Korea')
radio.pack()

root.mainloop()
print("Will it appear?\n",r.get())