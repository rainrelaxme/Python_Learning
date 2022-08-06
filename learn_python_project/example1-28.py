from tkinter import *

root = Tk()
def leftclick(event):
	print("x坐标轴位置：",event.x)
	print("y坐标轴位置：",event.y)
	print("相对于屏幕左上角x轴坐标：",event.x_root)
	print("相对于屏幕左上角y轴坐标：",event.y_root)
	
lab = Label(root, text = "hello", fg = 'red')
lab.bind('<Button-1>', leftclick)
lab.pack()

root.mainloop()
