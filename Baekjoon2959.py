import sys

nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

area = nums[0] * nums[2]

print(area) 
