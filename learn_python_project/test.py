# _*_ coding:utf-8 _*_
 
import pyglet
__author__ = 'admin'
 
'''
    python显示GIF图
'''
 
#   如果需要展示的GIF图未在工作目录下，这里需要先指明目标文件夹
pyglet.resource.path = [r'D:\learnpython']
#   animation中需要填入的是目标文件的文件名
animation = pyglet.resource.animation('changzhang.gif')
#   获取GIF图的实例
sprite = pyglet.sprite.Sprite(animation)
#   设定窗口的大小
win = pyglet.window.Window(width=sprite.width, height=sprite.height)
 
@win.event
def on_draw():
    win.clear()
    sprite.draw()
 
pyglet.app.run()