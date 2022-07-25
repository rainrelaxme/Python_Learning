import tkinter

root = tkinter.Tk()
label = tkinter.Label(root, text = 'hello,python')
label.pack()

button1 = tkinter.Button(root, text='BUTTON1')
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(root, text='BUTTON2')
button2.pack(anchor = tkinter.SE)
#button2.pack(side=tkinter.RIGHT)

root.mainloop()