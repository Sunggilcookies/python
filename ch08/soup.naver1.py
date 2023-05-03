# naver에서 필요한 정보 가져오기

import requests
from bs4 import BeautifulSoup

url ='https://www.naver.com/'
response = requests.get(url)
# print(response.text)
html = BeautifulSoup(response.text, 'html.parser')
# print(html)
print(html.title) #<Title>태그
print(html.title.text) # 태그 문자열
print(html.title.name) # 태그 이름

#'네이버를 시작페이지로' 문자열 찾아오기
div = html.find('div', attrs={'class': 'service_area'})
first_a = div.find('a')
print(first_a)
print(first_a.text)


#'주니어네이버' 찾아 오기
all_a = div.findAll('a')
print(all_a)
print(all_a[1].text)

for a in all_a:
    print(a) # 각각의 <a> 태그
    print(a.text) # 각각의 텍스트
