from tkinter import *
import tkinter.font

root=Tk()
ft=tkinter.font.Font(family='fixdays', size=30, weight='bold', slant='italic')
Label(root, text="hello python", font=ft).grid()
root.mainloop()