from tkinter import *

def printkey(event):
	print('你按下了：'+event.char)
	
root = Tk()
entry = Entry(root)
entry.bind('<KeyPress>', printkey)	
entry.pack()
root.mainloop()