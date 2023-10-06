""" In Here we will see a simple Project Based on oop """
class Product:
    def __init__(self) -> None:
       
        self.ProductStock = [{'Name':"Allu",'Quntity':10,'Weight':100,'Brand': None,'Price':40},{'Name':"Onion"'','Quntity':50,'Weight':200,'Brand':None,'Price':70},{'Name':"Rice",'Quntity':100,'Weight':1000},{'Name':"Flower",'Quntity':50,'Weight':100}]
    def __repr__(self) -> str:
        for itr in self.ProductStock:
            print (f"Name: {itr['Name']}, Quntity: {itr['Quntity']}, Weight: {itr['Weight']}")
        return f"Name: {itr['Name']}, Quntity: {itr['Quntity']}, Weight: {itr['Weight']}"
class Shop(Product):
    def __init__(self,name) -> None:
        self.name = name
        super().__init__()
    
    def add_Product(self,Name, Brand, Price,Weight,Quntity):
        self.Name = Name
        self.Brand = Brand
        self.Price = Price
        self.Weight = Weight
        self.Quntity = Quntity
        self.ProductStock.append({'Name': self.Name,'Price':self.Price,'Brand': self.Brand, 'Weight': self.Weight, 'Quntity': self.Quntity})

    def buy_Product(self,ProductName,Quntity,ammount):
        i = 0
        indexOfTheProduct = len(self.ProductStock)
        for itr in self.ProductStock:
            if itr['Name'] == ProductName:
                indexOfTheProduct = i
            i+=1

        if self.ProductStock[indexOfTheProduct]['Quntity'] > Quntity:
            QuntityWisePrice = Quntity * self.ProductStock[indexOfTheProduct]['Price']
            if QuntityWisePrice < ammount:
                ammount -= QuntityWisePrice
                print (f"Congrats You Just Buy {ProductName} in this {QuntityWisePrice} Price and you extra money is {ammount}")
            else:
                print(f"You don't enough Money ammount ot buy {ProductName} this in {ammount} price you need more {abs(ammount - QuntityWisePrice)} money to buy it")
        else:
            print(f"Don't Have Enough Quntity of this product")

Mobileshop = Shop("Gadget Shop")
Mobileshop.add_Product("Monitor","Sony",20000,1.5,100)

Mobileshop.buy_Product('Monitor',1,100000)
Mobileshop.buy_Product('Allu',5,1000)
Mobileshop.buy_Product('Onion',5,1000)