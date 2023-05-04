# 계산기 - 간단한 숫자 표시
# def cmd 함수를 이용해서 입력된 문자를 인수로 변환
from tkinter import *

def click(key):
    #값 받을때는 문자로 계산할때는 숫자로 다시 출력할때는 문자로
    if key == '=':
        try:
            value = eval(display.get()) # 입력된 게산값을 eval을 통해서 숫자로 변환하여 계산하여 value저장
            result = str(value)[0:10] # value에 저장된 계산값을 str을통해 문자열로 변환
            # 소수점 포함 10자리까지 출력
            display.insert(END, '=' +result)
        except:
            display.insert(END, "-->오류") #예외 처리
    elif key == 'C':
        display.delete(0, END) #맨 처음부터 삭제
    elif key == '<-':
        display.delete(-1, 1) #-1위치에 1개삭제

    else:
        display.insert(END, key)



root = Tk()
root.title("나의 계산기")

# top_row 프레임
top_row = Frame(root)
top_row.grid(row=0, columnspan=2, sticky=N) #N-NORTH 북쪽
display = Entry(top_row, width=50, bg='lightgreen')
display.grid(row=0, column=0 )

num_pad =Frame(root)
num_pad.grid(row=1, column=0, sticky=W) #W-WEST (서쪽)

num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
]
r = 0
c = 0

for btn_text in num_pad_list:
    def cmd(x=btn_text): # 함수에 인수(버튼 키)를 전달
        click(x)
    Button(num_pad, text=btn_text, width=11 ,height=3 , command=cmd).grid(row=r, column=c)
    c = c+1
    if c > 2: #column이 2(3열) 보다 크면 0(1열)로 이행
        c=0
        r = r+ 1 # row(행) 1증가

# 연산자 프레임
operator = Frame(root)
operator.grid(row=1, column=1, sticky=E)
operator_list = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C', '<-'

]
r = 0
c = 0

for btn_text in operator_list:
    def cmd(x=btn_text): # 함수에 인수(버튼 키)를 전달
        click(x)

    Button(operator, text=btn_text, width=5, height=3,
           command=cmd).grid(row=r, column=c)
    c = c+1
    if c > 1: #column이 1(2열) 보다 크면 0(1열)로 이행
        c=0
        r = r+ 1 # row(행) 1증가

root.mainloop()