#turtle 모듈
import turtle as t
t.shape("turtle")
t.bgcolor('black')
t.color('green')
t.speed(0) #0~10까지의 속도 0이가장ㅃ빠름

for x in range(100):
    t.circle(150)
    t.left(2)
t.mainloop()

