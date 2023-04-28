#try ~ except ~finally 구문
# error가 있으면 except 구문을 실해아고, 없으면
# try ~else ~를 실해앟마.
try:
    with open("../ch06/output/kbo2023.txt", 'r') as f:
        team = f.read()
except FileNotFoundError as e:
    print(e)
else:
    for i in team:
        print(i, end="")