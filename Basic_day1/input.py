# print('Now I need money')
# input()

# input('Give me some money: 5')

# money = input('Give me some money: ')
# print("here is your money", money)

first_money =input('kodom ali dosto, dosto kisu tk : ')
second_money =input('Shifa, kisu tk de: ')

print(type(first_money))
# by default the user input user will be string type 
first_money_int = int(first_money)
second_money_int = int(second_money)

print('money i got', first_money, 'and', second_money)
# total = first_money + second_money
total = first_money_int + second_money_int
""" 
Google search
1. convert to number string: str
2. convert decimal number: float
list,tuple etc
3. python int vs float

"""
print('total money i got: ', total)
print(type(first_money_int))