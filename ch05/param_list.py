# 리스트의 합계, 최대값, 최소값
# 리스트의 합계 연산하는 함수 w정의 - get_sum()
# 매개변수 - 리스트
def get_sum(a):
    sum_v = 0
    for i in a:
        sum_v += i
    return sum_v



#리스트의 평균을 계산하는 함수


def get_avg(a):
    sum_v = 0
    for i in a:
        sum_v += i
    return sum_v / len(a)


#최대값
def get_max(a):
    max_v = a[0] #리스트의 첫번째 값을 최대값으로 설정
    for i in v:
        if max_v < i:
            max_v = i
    return max_v

#최대값
def get_min(a):
    min_v = a[0] #리스트의 첫번째 값을 최대값으로 설정
    for i in v:
        if min_v > i:
            min_v = i
    return min_v

#리스트의 최대값의 위치 구하는 함수
def get_max_idx(a):
    max_idx = a[0] #첫번쨰값을 최대값의 위치로 설정
    for i in range(1, len(a)):
        if a[max_idx] < a[i]:
            max_idx = i
    return max_idx #for문 종료시 return
#출력
v=[3, 2, 5, 1, 4]
print(len(v))
print("합계 : ", get_sum(v))
print("평균 : ", get_avg(v))
print("최댓값 : ", get_max(v))
print("최솟값 : ", get_min(v))
print("최대값의 위치 : ", get_max_idx(v))
