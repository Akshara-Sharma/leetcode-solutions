class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        i = 0
        Sum = 0
        while i < len(nums):
            Sum = Sum + nums[i]
            nums[i] = Sum
            i+=1
        return(nums)

Output = Solution().runningSum(nums= [1, 1, 1, 1])
print(Output)