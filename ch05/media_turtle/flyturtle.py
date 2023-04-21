#거북이 대포 게임
#1.키보드 방향키로 발사 각도를 조절하고 스페이스 바로 대포를 발사 화살촉 모양으 ㅣ포탄이 하늘로 날라간다.
#2,화살촉 모양의 대포가 날라감
#3.스페이스바로 발사, 키보드 방향키로 발사 각도 조절
import turtle as t
import random

def turn_up():  #위쪽 화살표
    t.left(20)
def turn_down(): #아래쪽 화살표
    t.right(20)

def start():
    ang = t.heading()  #거북이가 바라보는 현재각도
    while t.ycor() > 0: #y좌표가 0보다 크다 - 포탄이 땅 위에 있는 동안
        t.forward(15)
        t.right(5)
    d = t.distance(target,0) #target 부터 t의 현재 위치까지의 거리
    print(t.distance)
    if d < 25: #명중
        t.color("blue")
        t.write('good', True, "CENTER", ("",15))
    else: # 목표지점에 닿지않았을 경우
        t.color('red')
        t.write('BAD', False, "CENTER", ("",15))
        t.color('black')
        t.goto(-200, 10)
        t.setheading(ang) #기억된 머리각도 설정
#땅그리기
t.goto(-300,0)
t.goto(300,0)

#목표지점 그리기
target = random.randint(50,150) #50~150사이의 x좌표 한 지점
t.color('green')
t.pensize(2)
t.up()
t.goto(target-25,2) #target =100, 100-25 =75
t.down()
t.goto(target+25,2) #target =100, 100+25 = 125 50px

t.color('black')
t.up()
t.goto(-200,10) #시작위치
t.setheading(20)


#거북이 대포가 동작하는 데 필요한 설정
t.onkeypress(turn_up,'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(start, 'space') #스페이스 키 누르면 발사
t.listen()

t.mainloop()