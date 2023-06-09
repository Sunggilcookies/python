# 거듭제곱 계산이 추가된 계싼기
from classfication.calculator2 import Calculator


class MoreCalculator(Calculator):
    #2x2x2x2
    def pow(self):
        num = 1
        for i in range(0, self.y):
            num = num * self.x
        return num
    '''
    def pow(self):
        return self.x ** self.y
        '''
    def div(self):
        # if self.y == 0:
        #     return 0
        #
        # else:
        #     return self.x / self.y
        try:
            return self.x / self.y
        except ZeroDivisionError:
            return "0으로 나눌수 없습니다."

cal = MoreCalculator(2,4)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())
print(cal.pow())

cal2 = MoreCalculator(5,8)
print(cal2.add())
print(cal2.sub())
print(cal2.mul())
print(cal2.div())
print(cal2.pow())
