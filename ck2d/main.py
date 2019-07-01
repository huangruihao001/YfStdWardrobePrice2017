from tkinter import *
import PriceFactor
import sys


def set():
    new_e = e.get()
    print("新系数为" + new_e)
    PriceFactor.set_factor(new_e)
    global b
    b.configure(state='disabled')
    b["text"] = "done"



root = Tk() # 初始化Tk()
root.title("PriceFactor")    # 设置窗口标题
# root.geometry("200x300")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=False, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
l = Label(root, text="Set pricefactor")
l.pack()   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
e = Entry(root)
e.insert(0, PriceFactor.get_factor())
e.pack()   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
b = Button(root, text="OK",  command = set)
b.pack()
root.mainloop() # 进入消息循环