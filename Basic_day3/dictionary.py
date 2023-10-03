numbers = [34, 21, 34, 56, 67, 43, 34]
person1 = ['kalachan','kaliakur',23,'student']
# key value pair
# dictionary
# object
# hash table
# overlap with set
# {keys,values,keys,values,keys}
person= {'name':'kala pakhi', 'address':'kaliapur','age':23, 'job':'facebooker'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language'] = 'python'
person['name'] = 'sada pakhi'
del person['age']
# special dictionary looping
print(person)

for keys,values in person.items():
    print(keys,values)