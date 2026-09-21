nums = [1,2,3]

i = len(nums) - 1

while i >= 0:
    if nums[i] == 9:
        nums[i] = 0
        i -= 1

    else:
        nums[i] += 1
        break

if i < 0:
    nums.insert(0, 1)

print(nums)