for i in range(0,5):
    for j in range(1,6):
        print(j+i*5, end=' ') #5는j의 종류값
    print('\n')

row = 5
col = 5 #좌석번호
for i in range(0,row):
    for j in range(1,col+1):
        print(col*i+j, end=' ') #5는j의 종류값
    print('\n')
