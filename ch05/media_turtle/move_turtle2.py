#turtle 모듈
import turtle as t
t.shape("turtle")

t.bgcolor('orange')

n = 4
d = 100


for i in range(n):
    t.forward(d)
    t.right(360/n)


t.mainloop()

