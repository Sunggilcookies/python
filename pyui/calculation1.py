# 계산기 - 간단한 숫자 표시

from tkinter import *


def click1():
    display.insert(END, '1')

def click2():
    display.insert(END, '2')

def click3():
    display.insert(END, '3')

root = Tk()
root.title("나의 계산기")



# 출력창
display = Text(root, width=30, height=1, bg='light green')
display.grid(row=0,columnspan=4)



Button(root, width=5, text='1', command=click1).grid(row=1, column=0)
Button(root, width=5, text='2', command=click2).grid(row=1, column=1)
Button(root, width=5, text='3', command=click1).grid(row=1, column=2)
Button(root, width=5, text='4', command=click1).grid(row=2, column=0)
Button(root, width=5, text='5', command=click1).grid(row=2, column=1)
Button(root, width=5, text='6', command=click1).grid(row=2, column=2)
Button(root, width=5, text='7', command=click1).grid(row=3, column=0)
Button(root, width=5, text='8', command=click1).grid(row=3, column=1)
Button(root, width=5, text='9', command=click1).grid(row=3, column=2)


root.mainloop()