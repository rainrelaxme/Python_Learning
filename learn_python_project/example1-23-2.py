from tkinter import *

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
root = Tk()
f=Frame(root, height=400, width=400)
f.color=0
f['bg'] = colors[f.color]
lab1=Label(f,text='0')
lab1.pack()

def foo():
	f.color = (f.color+1)%(len(colors))
	lab1['bg'] = colors[f.color]
	lab1['text'] = str(int(lab1['text'])+1)
	f.after(500, foo)
	
f.pack()
f.after(500,foo)
root.mainloop()