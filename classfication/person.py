# Person 클래스
# 클래스안에 함수가들어가있음 / 함수안에 변수들 생성 /
class Person:
    def __init__(self, name, age): #생성자 (함수)
        self.name = name  #초기화
        self.age = age

    #맴버의 정보
    def __str__(self):
        return  f"이름: {self.name}, 나이: {self.age}"


#상속 - 자식 클래스이름(부모클래스)
class Employee(Person): #상속하기
    def __init__(self, name, age, id):
        super().__init__(name, age) # 부모클래스의 맴버 상속Person의 부모init을 super함수로 넣어줌
        self.id = id #자식클래스 사변 초기화

    # 메서드 재정의(오버라이딩)
    def __str__(self):
        # return f"emp이름: {self.name}, 나이: {self.age}, 사번: {self.id}"
        return f"{super().__str__()}, 사번: {self.id}"
    def work(self):
        print('회사에 갑니다.')

e1 = Employee("이하나", 25, 'a1001')
e2 = Employee("김민식", 25, 'a1001')
print(e1)
e1.work()
print(e2)

# 클래스 사용 - 객체 생성(메모리 실행)
# p1 - 인스턴스이면서 오브젝트(객체)
p1 = Person("김산", 21)
print(p1)
