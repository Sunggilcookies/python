class City:
    a = ['Seoul', 'Incheon', 'Daejon', 'Jeju'] #클래스 리스트


str1 = ""
for i in City.a: #클래스리스트는 클래스 이름으로 직접 접근 (개채생성)
    str1 += i[0]            # ex c= City()


print(str1)


