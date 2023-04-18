#입력 처리
'''
print("당신이 좋아하는 색깔은 무엇이에요?(흰색)")
color=input()
print(color)

color = input("당신이 좋아하는 색은?")
print("좋아하는 색깔은", color, "입니다")
'''

#int() - 문자를 정수로 바꿔줌 숫자랑 + 는 안
number = int(input("숫자를 입력하세요"))
print('입력된 수는',(number + 4) ,'입니다.')
print('입력된 수는'+str(number + 4) + '입니다.')
