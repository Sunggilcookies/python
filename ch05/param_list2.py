# 2차원리스트 - 3행 2열(표 형태로 인식)
a = [
    [10, 20],
    [30, 40],
    [50, 60]
]
# #c출력
print(a[0][0]) #10
print(a[0][1]) #20
print(a[1][0]) #30
print(a[1][1]) #40
#
#2차원 리스트에 요소 추가 - 리스트를 추가함
a.append([70, 80])

# 전체 출력
print(a)

for x,y in a:
    print(x,y)

#리스트의 연산(합계)
total = 0
count = 0 #2차원 이상은 개수를 직접 카운트
for i in range(0, len(a)): #len(a)=3-1=2
    for j in range(0, len(a[i])):
        count +=1
        total += a[i][j]
    print()
#평균 구하기
avg = total / count
print(f'합계 : {total}')
print(f'개수:{count}')
print(f'평균{avg}')
'''
    i=0 j=0 0+10, total = 10
        j=1 10+30 total = 40
    i=1 j=0 30+50 total = 80
        j=1 30+70 total = 100
    i=2 j=0 100+20, total = 120
        j=1 120+40 total = 160
    i=3 j=0 160+60 total = 220
        j=1 220+80 total = 360
    
        
    
'''

#
# b= [1, 2, 3, 4]
# b.append(10)
# print(b)
#
#
# # print(len(b))
# #3차원리스트의 크기
# print("2차원 리스트 크기 (행)", len(a))
# print("2차원 리스트 크기 (열)", len(a[0]))
# print("2차원 리스트 크기 (열)", len(a[1]))
#
# #for ~ range()
# for i in range(0, len(a)): #len(a)=3
#     for j in range(0, len(a[i])):
#         print(a[i][j], end=' ')
#     print()
#
