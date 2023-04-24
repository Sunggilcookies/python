#turtle 모듈
import turtle as t
t.shape("turtle")

def polygon(n): #매개변수 도혀의 변의 개수
    for x in range(n):
        t.forward(50)
        t.left(360/n)
def polygon2(n,d):
    for i in range(n):
        t.forward(d)
        t.left(360/n)



polygon(3)
polygon(5)
'''
t.penup()
t.forward(100)
t.pendown()

polygon2(3, 100)
polygon2(5, 100)
''''''
for i in range(30):
    for x in range(3):
        t.forward(50)
        t.left(40)
        t.up()  # 펜올리기
        t.left(40)
        t.forward(20)
        t.left(60)
        t.down()  # 펜 내리
    for x in range(3):
        t.forward(10)
        t.left(35)
        t.up()  # 펜올리기
        t.left(10)
  '''
t.mainloop()

