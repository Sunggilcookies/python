x = ()
print(x)

x = (1,)
print(x)

x = (1,2,(3,4))
print(x)

x=(1,2,(3,4),(5,6))
print(x[3][1])


x=[1,2,3,4]
print(id(x))
x[0] = 5
print(id(x))