str = input()


def reverse(string):
    string = string[::-1]
    return string


def reverse2(s):
    if (len(s) == 0):
        return s
    else:
        return reverse(s[1:]) + s[0]


word = ''
for i in range(0, len(str)):
    if (str[i] != ' '):
        word += str[i]
    else:
        print(reverse2(word), end=" ")
        word = ""

print(reverse2(word))