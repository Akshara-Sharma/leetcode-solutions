nums = [1, 3, 4]

val = 4
i = 0

while i < len(nums):

    if val == nums[i]:
        break

    elif val < nums[i]:
        break

    else:
        i += 1

print(i)