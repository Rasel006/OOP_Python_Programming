n = int(input())

nums = list(map(int, input().split()))

minNum = min(nums)
maxNum = max(nums)

temp = minNum
maxIdx = nums.index(maxNum)
nums[nums.index(minNum)] = maxNum
nums[maxIdx] = temp

for i in range(0, n):
    print(nums[i], end=" ")