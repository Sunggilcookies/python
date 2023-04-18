#연습문제
#2월 29일 - 윤년, 4년마다 오죠 100년 대 x
#400년은 , 윤년이다.
#조건 1 - 4년마다 오고
#조건 2 100년단위는 윤년인아니나
#400년 단위로 윤년이다.
try:
    year = int(input("년도를 입력하세요"))
    e = year % 4
    if (e==0 and year % 100 != 0) or (year % 400 ==0):
        print(f'{year}년은 윤년입니다.')
    else:
        print(f'{year}년은 윤년이 아닙니다.')
except ValueError:
    print("숫자를 입력해 주세요")
