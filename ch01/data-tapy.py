# 주석
# 자료형 - 숫자, 문자, 불리언, 리스트, 객체
'''
print(12)
print(type(12)) # type()함수 <int - integer(정수형)>

print(3.3)
print(type(3.3)) # <float - 실수형>
'''

n = 1 # 변수 선언 방법 -자료형은 생략
print('n=', n, '개') #콤머(,)는 한 칸 띄움
print('n = ' + str(n) + '개') # str(숫자) - 문자로 변환함

msg = "좋은 하루!!"
print('메시지 :', msg)
print(type(msg)) # <class 'str'>

num = int('120') # int(문자형) - 숫자로 변환함
print(num)

num2 = int(120.7)
print(num2) # 120


state = True
print(state) #True
print(not state) #False

print(10 > 11) #False
print(10 < 11) #True
