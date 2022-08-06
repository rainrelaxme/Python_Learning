from tkinter import *

root = Tk()
def hello():
	print("You should click main menu.")

m= Menu(root)
for item in ['文件', '编辑', '视图', '帮助']:
	m.add_command(label=item, command=hello)
root['menu']=m
root.mainloop()