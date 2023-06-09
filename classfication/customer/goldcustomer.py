#GoldCustomer 클래스 생성
# 맴버 변수 - 고객아이디, 이름, 고객등급, 구매할인율, 보너스 적립율
from classfication.customer.customer import Customer


class GoldCustomer(Customer):
    def __init__(self, cid, cname):
        super().__init__(cid,cname)
        self.cgrade = "GOLD"
        self.sale_ratio = 0.1 #10%
        self.bonus_point = 0
        self.bonus_ratio = 0.02 # 2%

    def calc_price(self, price):
        #구매할인율
        #할인가격= price * sale_ratio(가격 = 가격 * 구매할인율)
        #할인된가격 = 원래가격 - (원래가격 * 구매할인율)
        price = int(price - price * self.sale_ratio) #가격
        self.bonus_point += int(price * self.bonus_ratio) #적립금
        return price

if __name__=="__main__":
    g1 = GoldCustomer(1003, "뷔")
    price3 = 10000
    cost3 = g1.calc_price(price3)
    print(f'{g1.cname}님의 구매비용은 {cost3}입니다.')
    print(g1)


