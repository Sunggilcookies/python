#객체 지향언언 - 캡슐화(정보은닉), 상속, 다형성
#Counter 클래스 만들기
# 맴버 변수에 직접 접근하지 않음 - 정보 은닉(캡슐화)
# 함수안에 맴버변수를 작성 - set(), get()
#외부에서는 함수에 접근
class Counter:
    x = 0

    def __init__(self):
        Counter.x += 1 #클래스변수이므로 클래스로 직접 접근

    def get_count(self):
        return Counter.x

c1 = Counter()
# print(c1.x)#맴버 변수에 접근하지 않음
print(c1.get_count())

c2 = Counter()
print(c2.get_count())

c3 = Counter()
print(c3.get_count())








'''
class Counter:
    def __init__(self):
        self.x=0
        self.x += 1 #x에 1증가

    def get_count(self):
        return self.

c1 = Counter() #객체 생성
print(c1.get_count()) #1

c2 = Counter() #객체 생성
print(c2.get_count()) #2'''