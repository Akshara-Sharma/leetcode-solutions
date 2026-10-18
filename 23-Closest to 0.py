class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        i = 0
        value1 = nums[i]

        for i in range(len(nums)):
            if abs(value1) > abs(nums[i]):
                value1 = nums[i]
            elif abs(value1) == abs(nums[i]) and nums[i] > value1:
                value1 = nums[i]

        return(value1)

Output = Solution().findClosestNumber(nums = [-4,-2,1,4,8])
print(Output)