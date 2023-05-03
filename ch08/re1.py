#re 모듈을 임포트함
import re

# /정교표현식/g -> re.compile("정규표현식")
# 소문자 a부터 z까지 일치하는 문자를 반복해서 찾음
# match() - 일치하는 문자를 찾는 함수
# search()- 전체 중에 특정문자가 일치하면 찾음 match와 다르게 순서상관 없음
p = re.compile("[a-z]+")


m1 = p.match('afternoon')
print(m1) #m1 객체
print(m1.group()) #문자열 출력

m2 = p.match('2023 good luck')
print(m2) #숫자로 시작해서 못찾음


s1 = p.search('2023 good luck')
print(s1)
print(s1.group())


