t = int(input())
for i in range(0, t):
    x, y = (input().split())
    x = int(x)
    y = int(y)
    start = min(x, y)
    end = max(x, y)
    sum = 0
    for num in range(start+1, end):
        if (num % 2 != 0):
            sum += num
    print(sum)