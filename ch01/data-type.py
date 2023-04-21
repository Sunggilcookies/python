#주석
#자료형 - 숫자, 문자, 불리언, 리스트, 객체
# 여러줄 주석: 쌍따옴표 3개
"""
print(12)
print(type(12)) # type()함수 <int - interger(정수형)
      



print(3.3)
print(type(13.3) # <float - 실수형>
"""
n = 1 #변수 선언 방법 - 자료형은 생략
print('n =' , n, '개' )
print('n = ' +str(n) +'개')

msg = "좋은 하루!!"
print('메세지 : ',msg)
print(type(msg))

num = int('120') #int(문자형) - 숫자로 변환함
print(num)

num2 = int(12.7) #12
print(num2)

# 불리언(참/거짓)
state = True
print(state) #True
print(not state)  #False

print(10>11) #False
print(10<11) #True
