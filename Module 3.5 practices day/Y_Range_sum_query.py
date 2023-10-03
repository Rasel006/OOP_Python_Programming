n, t = map(int, input().split())

nums = list(map(int, input().split()))
prefix_sum = [nums[0]]


for i in range(1, len(nums)):
    prefix_sum.insert(i, nums[i] + prefix_sum[i-1])

for i in range(0, t):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    sum = 0
    if (l == 0):
        sum = prefix_sum[r]
    else:
        sum = prefix_sum[r] - prefix_sum[l-1]
    print(sum)