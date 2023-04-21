#random 모듈
# ~10 :random.randint(1,10)
import random

# # 주사위 만들기
# dice = random.randint(1, 6)
# print(dice)

# 로또 번호 생성하기
for i in range(10): #0~9
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1+dice2

    if total==7:
        print('Seven Thrown!!')
    if total==11:
        print('Eleven Thrown')
    if dice1 == dice2:
        print('DoubleThrown!!')

    print(str(dice1)+' ')
    print(str(dice2) + '\n')
# #리스트에서 랜덤하게 값을 추출하기
# 과일 = ['딸기', '수박', '참외', '사과']
# # print(과일[-1]
# print(random.choice(과일))

#주사위 2개를 10번 던지기
# 두눈의 합이 7이면 "Seven Thrown!!" 출력 , 11이면 Eleven Thrown" 출력
# 두눈의 수가 같으면 "Double Thrown!!"출력