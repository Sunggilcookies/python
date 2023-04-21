import turtle as t
t.shape('turtle')
t.bgcolor('black')
t.speed(0)
for x in range(2000):
    if x % 3 ==0:
        t.color("white")
    if x % 3 ==1:
        t.color("red")
    if x % 3 ==2:
        t.color("green")
    t.forward(x*2)
    t.left(130)

t.mainloop()