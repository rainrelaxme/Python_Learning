from tkinter import *

root=Tk()
root.title("登录")
root['width'] = 200
root['height'] = 80

Label(root, text="用户名",width=6).place(x=1,y=1)
Entry(root, width=20).place(x=45,y=1)
Label(root, text="密码", width=6).place(x=1,y=20)
Entry(root, width=20,show="*").place(x=45,y=20)

Button(root,text="Login", width=8).place(x=40,y=40)
Button(root,text="Cancel", width=8).place(x=110, y=40)

root.mainloop()