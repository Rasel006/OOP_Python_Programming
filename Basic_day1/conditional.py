# no, not, not in, is, is not
# <, >, >=, <=, ==, !==
# and, or use korte pari
a = 1
boss = False

if a > 5:
    print('5 er beshi')
    print('koto beshi k jane')
elif a > 3:
    print('olpo boro')
elif a == 2:
    print('akdom dui er soman soman')
else:
    print('chuto chuto lombi lombi ratee')    

if boss is not True:
    print('lunch er pore ashen')
else:
    print('tell er bakso niye asteci boss re tell dio')

# if boss not True:
#     print('tell er bakso niye asteci boss re tell dio')
# else:
#     print('lunch er pore ashen')

# nested condittion
coin='head'
if boss == True:
    print('boss you are joss')
    if coin == 'tail':
        print('bowling')
    else:
        print('batting')
        if 5 > 2 or boss!=True:
            print('do something')
            if 8%2==0 and 5%2==1:
                print('even 8 is an even number')


else:
    print('you are loss not a boss') 


