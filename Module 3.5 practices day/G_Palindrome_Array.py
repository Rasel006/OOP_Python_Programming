n = int(input())

nums = list(map(int, input().split()))

flag = True

i = 0
j = n-1
while (i < j):
    if (nums[i] != nums[j]):
        flag = False
        break
    i += 1
    j -= 1

if (flag):
    print("YES")
else:
    print("NO")