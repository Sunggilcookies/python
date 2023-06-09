# 구구단 쓰기
# with~ as 구문에서는 f.close{}를 tkdydgkwl dksgdma
try:

    with open("./output/gugu.txt", 'w') as f:
        for i in range(2, 10):
            for j in range(1, 10):
                gugudan = f'{i} x {j} = {i*j}\n'
                f.write(gugudan)
            f.write('\n')
except FileNotFoundError:
    print("파일을 쓸 수 없ㅅ습니다.")

# 파일 읽기
with open("./output/gugu.txt", 'r') as f:
    gugudan = f.read()
    print(gugudan)