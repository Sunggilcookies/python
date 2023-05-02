
from tkinter import *
from classfication.extend.converters import Converter
def convert():
    try:
        temp_c = eval(ent_c.get()) #eval-문자열매개변수를 숫자로 변환
        txt_f.delete(0.0, END)
        temp_f = temp_c * 1.8 +32
        temp_f = "{: .1f}F".format(temp_f) #소수자리수 설정
        txt_f.insert(END, temp_f)

    except NameError:
        txt_f.inser(END, "오류")



root = Tk()
root.title("온도 변환기")
root.geometry("240x80+100+100")

Label(root, text='deg C').grid(row=0, column=0)
ent_c = Entry(root, width=15)
ent_c.grid(row=0, column=1)

Label(root, text='deg F').grid(row=1, column=0)
txt_f = Text(root, width=15, height=1)
txt_f.grid(row=1, column=1)

Button(root, text='변환', width=10, command=convert).grid(row=2, columnspan=2)

root.mainloop()