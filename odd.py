import random

nums = []
odds = []
for i in range(500):
    x = random.randint(1, 100)
    nums.append(x)

for i in range(500):
    if nums[i] % 2 == 1:
        odds.append(nums[i])

print(nums)
print(odds)