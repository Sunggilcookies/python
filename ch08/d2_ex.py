# 2차원 리스트
'''
d = [
    [10, 20],
    [30, 40],
    [50, 60],




]
# 3행 2열
print(d[0][0]) #10
print(d[1][1]) #40
print(d[2][0]) #50

# [70,80]을 추가

# 2차원 리스트 객체 출력
print(d)

# 저체 요소(값) 출력
for x, y in d:
    print(x, y)

    #리스트 이름 = [요소1, 요소2, [값1, 값2]]
e = [7, 3, ['chicken', 'eagle', 'monkey']]

print(e[1]) #3
print(e[-1]) #['chicken', 'eagle', 'monkey']

# eagle 출력
print(e[-1][1])
'''

# 2차원 리스트 - 성적 통게
# 5명의 수학, 영어 과목의 총점과 평균
score = [
    [80, 70],
    [70, 85],
    [60, 90],
    [50, 75]
]
# 개인별 총점과 평균
total = 0

# 수학 - 1열
# 영어 - 2열
print("총점 평균")
n = len(score)
for i in range(0, 4): # 0,1,2, 3
    total = score[i][0] + score[i][1]
    print(total, total/2)

# 과목별 총점과 평균
sum_subj = [0,0] # sum subj[0] = 0(수학), sum_subj[1] =  0(영어)

for i in range(0, n):
    sum_subj[0] += score[i][0] #수학 합계
    sum_subj[1] += score[i][1] #영어 합계

print("총점 : 수학 영어 ")
print(f'\t  {sum_subj[0]}, {sum_subj[1]}')
print("평균 : 수학 영어 ")
print(f'\t  {sum_subj[0]/n}, {sum_subj[1]/n}')




