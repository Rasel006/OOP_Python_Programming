def full_name(first, last):
    name = f'{first} {last}'
    return name
# take parameter in order (serial wise)
# name = full_name('Alu','kodo')

name = full_name(last='Alu',first= 'kodo')
print(name)

# def famous (**kwargs)

def famous_name(first,last,title, **addition):
    name = f'{title} {first} {last}'
    print(addition)
    return name
name = famous_name(first='Taheri',last='Ali',title='hujur',additional='')
print(name)

# # return multiple things from an array

# def a_lot(num1, num2):
#     sum =num1 + num2
#     mult =num1 * num2
#     remain =num1 - num2
#     # return [sum,mult,remain]
#     return sum,mult,remain


# everything =a_lot(55,21)
# print(everything)
