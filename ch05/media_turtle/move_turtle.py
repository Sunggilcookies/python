#turtle 모듈
import turtle as t
t.shape("turtle")




for i in range(0,4):
    t.forward(100)
    t.left(90)
t.color("blue")
for i in range(0,3):

    t.forward(100)
    t.left(120)
t.color("red")
t.forward(50)
t.pensize(3)
t.circle(50)


t.mainloop()

