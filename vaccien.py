'''year = input("출생년도 네자리를 입력 띠어쓰기로 한글자씩")
age = 2023-int(year)+1
if(age>=20 and age<=65):
    print('백신접종대상')
    if year[-1]=='1' or year[-1]=='9':
        print('월요일')
    elif year[-1]=='2' or year[-1]=='8':
        print('화요일')
    elif year[-1]=='3' or year[-1]=='7':
        print('수요일')
    elif year[-1]=='4' or year[-1]=='6':
        print('목요일')
    else:print('금요일')
else: print("하반기 일정 확인")
'''
#입력
name = input("이름")
user_id = input('아이디')
pw = input('비밀번호 : ')
id_card1 = input('주민번호 앞자리 입력 : ')
id_card2 = input('주민번호 뒷자리 입력 : ')
print("=" * 30)

#출력
print("이름 : {}".format(name))
print("아이디 : {}".format(user_id))
pw = '*'*len(pw)
print("비밀번호 : {}".format(pw))
id_card2 = id_card2 [0] + ('*' * 6)
print("주민등록번호 : {0}-{1}".format(id_card1, id_card2))
