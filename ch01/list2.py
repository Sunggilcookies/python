print('hi')
# 문자열 관련함수
# split(구분기호) -> 문자열이 리스트로 변환
# 문자열.split()
fruit = "banana, apple, strawberry"
fruitlist = fruit.split(',')

print(fruitlist)
print(fruitlist[1]) # 1번 인덱스 -> apple

# 문자열.replace('이전문자', '새문자')
str1='hello world'
str1=str1.replace('world','korea')
print(str1)
#format()함수
str2 = "My name is {0} I am{1} years old".format('Mario',40)
'''str3 = "My name is %s." % '하하
name="Mario"

str4 = f"My name is {name}"

print(str3)
print(str4)'''
print(str2)
''''
#split() - ':' 로 구분하고 리스트로 변경
string = "a:b:c:d"
string2 = string.split(':')
print(string2[-1])

# 두 수를 동시에 입력 받아서 더하기
n1, n2 = input("두수입력하세요 ").split()
add = int(n1) + int(n2)
print(add)
'''
#find() - 문자열이 존재하는 위치 반환
text='hello'
print(text.find('h')) #0
print(text.find('l')) #2
print(text.find('k')) #-1

print(text.find('hello'))

