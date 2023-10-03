class Phone:
    menufactured = 'Chaina'
# constructor
    def __init__(self,owner,brand,price):
        self.owner =owner
        self.brand = brand
        self.price = price
    
    def __send_sms(self,phone,sms):
        text = f'sendind sms to:{phone} {sms}'
        print(text)
my_phone = Phone('Khala Chan','Oppo',9500)
print(my_phone.owner,my_phone.brand,my_phone.price)
her_phone = Phone('She','iphone',120000)
print(her_phone.owner,her_phone.brand,her_phone.price)
