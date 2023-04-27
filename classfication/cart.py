# Cart 클래스 정의
# 클래스 리스트
class Cart:
    li =[]

    def add_cart(self , goods):
        Cart.li.append(goods) # append 추가하는것
cart1 = Cart()
cart1.add_cart("계란")
print(Cart.li)
cart2 = Cart()
cart2.add_cart("그란")
print(Cart.li)
cart3 = Cart()
cart3.add_cart("란")
print(Cart.li)
for i in Cart.li:
    print(i)