nums = [1,2,3,4,5]
val = 5
i = 0

# if val == nums[i], then delete it. otherwise, keep it.

# for i in range(len(nums)):
while i < len(nums):
    if(val == nums[i]):
        del nums[i]
    else:
        i = i+1

print(nums)
k = len(nums)
print(k)
