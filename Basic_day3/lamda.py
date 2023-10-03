# lam da 

# def doubled(x):
#     return x*2

doubled = lambda num : num*2
squared = lambda num : num * num
result = doubled (44)
output= squared (9)
print(result, output)

add = lambda x,y : x+y
sum = add(34,11)
print(sum)

numbers = [12,56,67,43,67,12,98]
doubled_nums = map(doubled,numbers)
doubled_nums = map(lambda x:x*2, numbers)
squared_nums = map(lambda x:x*x, numbers)

print(numbers)
# print(list(doubled_nums))
print(list(squared_nums))

actors = [
    {'name':'sabana', 'age': 65},
    {'name':'sabnur', 'age': 45},
    {'name':'sabila nur', 'age': 30},
    {'name':'srabonti', 'age': 38},
    {'name':'shwaon', 'age': 47},
]

juniors = filter(lambda actor : actor['age'] < 40, actors)
Fivers= filter(lambda actor : actor['age']%5==0, actors)
# print(list(juniors))
print(list(Fivers))