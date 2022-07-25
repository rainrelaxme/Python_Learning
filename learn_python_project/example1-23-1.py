from tkinter import *

root=Tk()
root.title("使用Frame组件的例子")
f1 = Frame(root)
f1.pack()
f2 = Frame(root)
f2.pack()
f3 = LabelFrame(root, text="弟3个Frame")
f3.pack(side=BOTTOM)

redbutton = Button(f1, text="red", fg="red")
redbutton.pack(side=LEFT)
brownbutton = Button(f1, text='brown', fg="brown")
brownbutton.pack(side=LEFT)
bluebutton = Button(f1, text="blue", fg="blue")
bluebutton.pack(side=LEFT)
blackbutton = Button(f2, text="black", fg="black")
blackbutton.pack()
greenbutton = Button(f3, text="green", fg="green")
greenbutton.pack()

root.mainloop()