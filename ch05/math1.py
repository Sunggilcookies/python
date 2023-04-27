# 수학 모듈 - math
# 절대값, 올림, 내림, 제곱근, 원주율, random
import math

print(math.pi) #원주율
print(math.ceil(2.54)) #정수로 올림
print(math.floor(4.923)) #내림(버림)
print(math.sqrt(25)) #제곱근

# 내장 함수
print(round(11.78))

# 절대값
print(abs(-10))

# 절대값을 함수로 만들기
# 1. 알고리즘
"""
def my_abs(x):
    if x >= 0:
        return x
    elif x < 0:
        return -x
print(my_abs(7))
print(my_abs(-7))
"""

# 2. 알고리즘

def my_abs2(x):
    y = x * x
    return int(math.sqrt(y))

# 제곱수 -> 제곱근(실수로 표기)
print(my_abs2(7))
print(my_abs2(-7))
