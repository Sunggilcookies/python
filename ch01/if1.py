# 조건문
# 상향 연산자 - 조건 연산자 사용안함
# if문의 클론(:) 코드 블럭을 의미하고 다음줄에서 4칸 들여쓰기
'''
result = (10 < -10) ? 'T' : 'F'
print(result) '''
'''
x = 10
y = -10

if x > y :
    print('맞음')
else :
    print('틀림')
'''

# 자동차 주행 제한속도가 50km 이상이면 "안전속도 위반!!"
# 아니면 안전속도 준수
'''
limit_speed = 40
if limit_speed >= 50:
    print('안전속도 위반')
print("현재 속도는" + str(limit_speed)+("km입니다"))

'''
# 자동차 주행 제한속도가 50km 이상이면 "안전속도 위반!! 과태료 10만원 부과대상"
# 50km 미만이면 "안전 속도 준수"를 출력하는 프로그램
limit_speed = 50
if limit_speed >= 50:
    print("안전속도 위반!! 과태료 10만원 부과대상")
else:
    print("안전속도 준수")
    
