n = int(input())

nums = input()
nums = list(nums)
sum = 0

for i in range(0, n):
    sum += int(nums[i])

print(sum)