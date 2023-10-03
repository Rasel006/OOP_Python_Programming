name = 'Sakib\'s Khan' #escape
name2 = "Sakib Khan"
name3 = """
    sakib Khan
    number one

"""
print(name)

#string is a sequence of characters
for char in name2:
    print(char)
print(name2[3])
print(name2[1:6])
print(name2[-3])
print(name2[::-1])
# name2[0]='R'
# print(name2)
if 'Khan' in name2:
    print('exists')

    
print(name2.upper())

# mutable means changable
# immutable means you can not change it
