import turtle as t
import random
import time

# 주인공 거북이
t.shape("turtle")
t.setup(500, 500)  # width,height
t.bgcolor("orange")
t.color('white')
t.up()


#글자생성
dashtime = t.Turtle()
# 적 거북이 생성
te = t.Turtle()
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0, 200)

#먹이설정
tf = t.Turtle()
tf.shape('circle')
tf.color('green')
tf.speed(0)
tf.up()
tf.goto(0,-200)


def turn_left():
    t.setheading(180)
def turn_down():
    t.setheading(270)
def turn_up():
    t.setheading(90)
def turn_right():
    t.setheading(0)

#대쉬 설정
can_dash = True
last_dash_time = time.time()  # 마지막 대쉬 시간
dash_interval = 5  # 대쉬 간격

def dash():
    global can_dash, last_dash_time
    now = time.time()  # 현재 시간
    if can_dash and now - last_dash_time >= dash_interval:
        t.forward(50)
        can_dash = False  # 대쉬 불가능 상태로 변경
        t.color('white')
        last_dash_time = now  # 마지막 대쉬 시간 갱신
    elif now - last_dash_time < dash_interval:
        # 대쉬 불가능 상태이면서 대쉬 간격이 지나지 않은 경우
        dash_time_left = dash_interval - int(now - last_dash_time)
        dashtime.write(f'Dash time left: {dash_time_left}', font=('Arial', 16, 'normal'))
    else:
        dashtime.clear()  # 대쉬 시간 표시 제거
        # 대쉬 사용 후 대쉬 가능 상태로 변경

    if not can_dash and now - last_dash_time >= dash_interval:
        can_dash = True

def enable_dash():
    global can_dash
    can_dash = True  # 대쉬 가능 상태로 변경

def play():
    global can_dash, last_dash_time
    now = time.time()  # 현재 시간
    if not can_dash and now - last_dash_time < dash_interval:
        # 대쉬 불가능 상태이면서 대쉬 간격이 지나지 않은 경우
        dash_time_left = dash_interval - int(now - last_dash_time) # 대쉬 시간 계산
        dashtime.clear()
        dashtime.write(f'Dash time left: {dash_time_left}', font=('Arial', 16, 'normal'))
    else:
        dashtime.clear()  # 대쉬 시간 표시 제거
        t.color('blue')
    #적 거북이와 닿지 않으면 게임유지
    # 적 거북이와 닿으면 게임 멈춤
    if t.distance(te) >15:
        t.ontimer(play ,100) #0.1초 간격으로 계속 play 호출

    t.forward(10)
    te.forward(9)

    #적거북이가 주인공 거북이의 우치ㅣ를따라옴
    #방향을 알아채는데 20% 확률로 적용
    if random.randint(1, 5) == 4:
        ang = te.towards(t.pos())
        te.setheading(ang)

    #주인공 거북이가 먹이에 닿으면 새 위치에서 랜덤하게 나타남
    if t.distance(tf) < 12:
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x,y)


#방향키 설정
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, 'Down')
t.onkeypress(dash, 'space')

t.listen()
play()
t.mainloop()
