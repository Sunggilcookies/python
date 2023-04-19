# 자리배치
# 입장객 수, 좌석열, 줄수
#입장객수가 열수로 나누어 떨어지는 경우, 그렇지 않은 경우
customer = int(input("입장객을 입력하세요"))
col = int(input("좌석열을 입력해주세요"))

if customer % col == 0:
    row = int(customer / col)
    print(row)
else :
    #row = int(customer / col) +1
    row = int(customer / col)+1


#print ("줄 수:", row)
#좌석배치
for i in range(0,row):
    for j in range(1,col+1):
        #좌석번호가 입장객수보다 크면 빠져나옴
        num=col*i+j
        if num > customer:
            break
        print(f'좌석{num}', end=' ')
    print('\n')

