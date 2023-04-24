# Dog 클래스
class Dog:
    tricks = [] # 클래스 리스트
    def __init__(self, name):
        self.name = name
        # self.tricks = [] #인스턴스리스트 인스턴스를 쓰면 tricks 공유 저장 x 
    def add_tricks(self, trick):
        self.tricks.append(trick)



dog1 = Dog("기쁨")
dog2 = Dog("사랑")

dog1.add_tricks('몸 뒤집기')
print(dog1.name)
print(dog1.tricks)
dog2.add_tricks('죽은 척 하기')
print(dog2.name)
print(dog2.tricks)

