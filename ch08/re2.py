import re

# findall() - 문자열 검색 : 결과를 리스트로 반환

str = "Two is too"
m1 = re.findall("[wo]o", str)
print(m1) #['Two'}

m2 = re.findall("T[wo]o", str, re.IGNORECASE)
print(m2)

m3 = re.findall("T[^w]o", str, re.IGNORECASE) #[^w] - 'W'가 아닌 문자
print(m3)