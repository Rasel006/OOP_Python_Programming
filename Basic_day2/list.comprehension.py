numbers =[45,87,96,65,43,90, 85,14,26,61,70]
odds = []
for num in numbers:
    if num % 2 ==1 and num % 5 ==0:
        odds.append(num)
print(odds)
# not readable
odd_nums =[num for num in numbers if num % 2 ==1]
odd_nums =[num for num in numbers if num % 2 ==1 if num % 5 ==0]
print(odd_nums)
players =['shakib', 'mushfiq', 'liton']
ages =[38,37,32]

age_comp =[]
for player in players:
    print('player:',player)
    for age in ages:
        print(player,age)
        age_comp.append([player,age])
print(age_comp)

age_comp2 =[[player,age] for player in players for age in ages]
print(age_comp2)