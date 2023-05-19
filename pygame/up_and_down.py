# 숫자 추측게임
"""
게임방법
-게임이 시작되면 컴퓨터가 난수(정답)을 생성한다.
-사용자의 추측값이 정답과 같으면 '정답!',
추측값이 정답보다 크면 "너무 커요!",
추측값이 정답보다 작으면 '너무 작아요!' 출력
"""
import random
#컴퓨터의 난수 생성
com = random.randint(1,50) #com=정답
print(com)
#사용자의 추측값
min_v=1
max_v=50
chance = 10
i=0
while True:
    try:
        if (i < chance):

            guess = int(input(f"맞혀보시라요({min_v}~{max_v})>"))
            # 조건문 작성
            if (guess > com):
                print("너무 커요..")
                max_v = guess
                i += 1
                print(f"남은 횟수는{chance - i}입니다.")
            elif guess < com:
                print("너무 작아요.")
                miv_v = guess
                i += 1
                print(f"남은 횟수는{chance - i}입니다.")
            elif guess == com:
                print("정답입니다.")
                print(f"점수는{(chance - i) * 10}점입니다.")
                break
        elif chance - i == 0:
            print("gameover")
            break
    except ValueError:
        print("유효한숫자가아닙니ㅏㄷ. 다시입력해주세요")














