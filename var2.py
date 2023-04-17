# 변수 선언, 대입 연산자
# 변수 값 바꾸기
# 파란색 컵 1이 있고, 빨간색 컵 2가 있을때 두 값을 바꾸시오
# 임시 변수 - 노란컵
blue = 1
red = 2
'''
yellow = blue # yellow =
blue = red
red=yellow
print(red)
print(blue)'''
#파이썬 직접교환
blue, red = red, blue
print("blue =", blue, "red =", red)

print('*** 회원가입 ***')
userid = 'hangul'
userpw = 'han1234'
name = '한글'
phone = '010-1234-5678'
age = 35
print('*'*10)
print("아이디 :", userid)
print("비밀번호 :", userpw)
print("이름 :", name)
print("전화번호 :", phone)
print("나이 : "+ str(age))
#나이 : + 연산자 사용 출력
