import tkinter
win = tkinter.Tk()					#创建windows窗口对象	
win.title("我的第一个GUI程序")		#设置窗口标题
#win.geometry("800x600")			#设置初始大小，中间为英文字母x
win.minsize(400,600)				#设置窗口最小尺寸，用逗号隔开
win.maxsize(1440,800)
win.mainloop()
