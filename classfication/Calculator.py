#Calculator 클래스

class Calculator:
    def __init__(self):
        self.x = 0 #맴버 변수에 x를 할당

    def add(self, y):
        self.x = self.x + y
        return self.x

    def sub(self, y):
        self.x = self.x - y
        return self.x


cal1 = Calculator()
print(cal1.add(10))
print(cal1.sub(10))

cal2 = Calculator()
print(cal2.add(21))
print(cal2.sub(2.5))