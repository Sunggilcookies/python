#입력처리 - input()함수
#방법 1
"""
print("이름을 입력해주세요")
name =input() #문자 사용
print(name + "님 안녕하세요)

#방법 2
name=input("이름을 입력해주세요")
print(name)"""

#입력받은 문자열임 -> 정수로 변환 int 함수 사용
"""
nmber = (input("숫자를 입력해 주세요(1~10)"))
print(number * 2)"""

#두 수를 입력받아 합을 계산하기
"""
x= int(input("첫째 수 입력 : "))
y= int(input("둘째 수 입력 : "))
sum_v = x + y
print(sum_v)"""

#나이 계산 프로그램
#나이 = 현재년도 -출생년도 +1
'''
current_year = 2023
birth_year = int(input("태어난 년도를 입력해주세요"))

age= current_year - birth_year + 1

print(str(age)+'세');'''

#사각형을 계산하는 프로그램
garo = int(input("가로 길이를 입력해주세요"))
sero = int(input("새로 길이를 입력해주세요"))
넓이=garo*sero
print("사각형의 넓이"+str(넓이)+"입니다.")
