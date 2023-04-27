# 함수 - function, method(매서드)
import time
# # 1부터 11까지 출력
# for i in range(1, 11):
#     print(i)
#
# # 1부터 n까지 출력하는 함수 0부터 n임
# def get_num(n):
#     for i in range(1,n+1):
#         print(i, end=" ")
#
#
# get_num(11)
# print()

#1부터 n까지 합계를 구하는 함수
start= time.time()
def get_num(n):
    sum_v = 0
    for i in range(1, n + 1):
        sum_v += 1
    return sum_v

print(f'합계 : {get_num(1000000)}')
end = time.time()
print(f'소요시간 : {end-start}초')


#계산 복잡도 - 곱셈, 덧셈 , 나눗셈 -3번 :
start = time.time()
def get_sum2(n):
    sum_v = (n*(n+1)) // 2
    return sum_v
if __name__=="__main__":
    print(f'합계 : {get_sum2(100000000)}')
    end = time.time()
    print(f'소요시간 : {end-start}초')

#
# def get_sum2(n):
#     # sum_v = (n*(n+1) // 2)
#     return sum_v


