#sys 모듈 - system
#명령프롬포트

import sys

#입력값 연산
args = sys.argv[1:] #args 리스트 생성
print(args)


total = 0
for i in args:
    total += int(i) #입력 받은 문자를 숫자형으로 변환해야함

print(total)