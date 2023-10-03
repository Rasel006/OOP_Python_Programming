# self homework

# def call():
#     print('calculator')
#     return 'calculator done'

class calculator:
    brand ='Casio MS999'
    num1 = 34
    num1 = 23

    def add(self,num1,num2):
        sum = num1 + num2
        print ('Add method',sum)

    def deduct(self,num1,num2):
        subtract = num1 - num2
        print ('Deduct method',subtract)

    def multiply(self,num1,num2):
        multiplication= num1 * num2
        print ('multiply method',multiplication)

    def devide(self,num1,num2):
        divition= num1 / num2
        print ('divide method',divition)
    

my_calculator = calculator()
print(my_calculator.num1)

my_calculator.add(34,23)
my_calculator.deduct(34,23)
my_calculator.multiply(34,23)
my_calculator.devide(34,23)


# deduct method
# multiply method
# divide method