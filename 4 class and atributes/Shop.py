class Shop:
    cart = [] # cart is a class atributes 

    def __init__(self,buyer):
        self.buyer =buyer

    def add_to_cart(self,item):
        self.cart.append(item)

mehjabeen = Shop('Mehjabeeen')
mehjabeen.add_to_cart('shoes')
mehjabeen.add_to_cart('phone')
print(mehjabeen.cart)

nisho = Shop('Nishu')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)