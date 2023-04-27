# map(), filter()
# 리스트를 매개변수로 전달
#lamda 함수와 map() 사용
# map()함수는 list()를 이용하여 리스트로 만듬
#일반함수
def times(x):
    return 3 * x

v= [1,2,3,4]
# times2 = lambda x : 3 * x
result = map(times, v)
print(list(result))

#filter()와 lambda 사용
#음의 정수를 출력하시오
def negative(n):
    return n <0

li = [-5, 1, 2, -11, 76]

# negative = lambda x : x < 0
value = filter(negative, li)
print(list(value))