class Shop:
    shopping_mall = 'jamuna'

    def __init__(self,buyer):
        self.buyer =buyer
        self.cart = [] # cart is an instance atributes 

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


apurba = Shop('age pubo chilo')
apurba.add_to_cart('chiruni')
print(apurba.cart)