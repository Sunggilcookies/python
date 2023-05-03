#naver 메뉴 가져오기
import requests
from bs4 import BeautifulSoup

url = "http://www.naver.com"
response = requests.get(url)
print(response.text)
html = BeautifulSoup(response.text, 'html.parser')
print(html)

# 메뉴 - 메일, 카페, 블로그
menu_li = html.find('ul', attrs={'class':'list_nav type_fix'})
'''first_li = menu_li.find('li')
# print(first_li)
first_a = first_li.find('a')
print(first_a.text)
'''
#다른 메뉴 찾기 - findAll()
# all_li = menu_li.findAll('li')
all_a = menu_li.findAll('a')
for a in all_a:

    print(a.text)