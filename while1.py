# while 반복문
# 'hello'를 10번 출력
'''i = 0
while i < 10:
    print('hello')
    i = i+1'''

#1부터 10까지 더하기

'''
i=0
sum_v = 0
while i < 10:
    i += 1
    sum_v = sum_v + i
    print(i)

print(f'{sum_v}출력하기')
      
# 반복 조건문(break)
i = 1
sum_v = 0
while True:
    i += 1
    if i > 10:
        break
    sum_v += i
    print(f'반복 횟수{i}')
        
print(f'합계 : {sum_v}')
    '''
    
#반복을 계쏙 할까요?

while True:
    a=input("반복을 계속 할까요?(y/n)")
    if a == 'y':
        print('반복됩니다.')
    elif a == 'n':
        print('탈출!')
        break;
    
