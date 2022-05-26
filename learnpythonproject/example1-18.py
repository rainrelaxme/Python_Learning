from tkinter import *
from PIL import Image, ImageTk

win = Tk()
win.title("我的窗口")
lab1= Label(win, text = "你好", anchor = "nw")
lab1.pack()
#显式内置的位图
lab2 = Label(win, bitmap = 'question')
lab2.pack()

#显式自选的图片
bm = PhotoImage(file = r'D:\learnpython\learnpythonproject\material\bean curd.gif')
#借助pillow打开图片
#bm =Image.open(r'D:\learnpython\learnpythonproject\material\timg.jpg')
#bm = ImageTk.PhotoImage(bm)
lab3 = Label(win, image = bm)
lab3.bm = bm
lab3.pack()
win.mainloop()

