# .csv comma separated value
# .text text file

# with open('message.text', 'w') as file:
#     file.write('I love you, python!')

# with open('message.text', 'a') as file:
#     file.write('I love you, python!')

with open('message.text', 'r') as file:
    text = file.read()
    print(text)