#for ~ in range()
# 1부터 10까지 출력
sum_v = 0
for i in range(1,11, 1):
    print(i, end=" ")
print('=' * 10)
for i in range(10,0, -1):
    sum_v +=i
    print(i, end=" ")
print(sum_v)
#1부터 10까지의 홀수 출력
'''for i in range(1,10,2):
    print(i)
for i in range(1, 11, 1):
    if(i % 2 ==1):
        print(i)

'''
num=[10, 50, 30, 70]

print(50 in num) #true
print(80 in num) #false
#리스트 출력
print(num)

# 전체 요소를 출력
for i in num:
    if i > 50:
        print(i)

food = ['짜장', '짬뽕', '간짜장']
for i in food:
    print(i)
    

city = ['Seoul', 'Incheon', 'Gwangju']
for i in city:
    print(i[1])


'''
# city[0] : 첫번쨰 i = SEOUL -> I[0] 'S'


'''

    
    
