# set : unique item collection. No duplicate
# list --> []
# tuple ---> ()
#  set --> {}

numbers = [12,56,67,43,67,12,98]
print(numbers)
numbers_set =set(numbers)
print(numbers_set)
numbers_set.add(55)
print(numbers_set)
numbers_set.remove(56)

for item in numbers_set:
    print(item)
if 9 in numbers_set:
    print('9 exists')
elif 98 in numbers_set:
    print('98 exists')

A = {1, 4, 7, 4, 8}
B ={4, 6, 9, 2}
print(A&B)
print(A|B)