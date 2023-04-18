# 다중 조건문 - if ~ elif ~ else
# 놀이공원 입장료 계산
# 8세미만 - 미취학 아동, 14세 미만 - 초등학생, 20세 미만 - 초, 중등 20세이상- 일반인
'''if ~ elif ~ else'''

print("♣놀이 공원 입장료 계산♣")
(age) = int(input("나이를 입력해주세요"))

if age<8:
      charge = 1000
      print("미취학 아동입니다.")
elif age<8 and age<14:
      charge = 2000
      print("초등학생입니다.")
elif age<14 and age<20:
    
      charge = 25000
      print("청소년입니다.")
        
else and age < 20:
      charge = 3000
      print("일반인입니다.")
#메인 영역
print("입장료는" + str(charge) + "입니다.")

        
