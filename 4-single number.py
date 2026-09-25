class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for num in nums:
            if (nums.count(num) == 1):
                return(num)

Output = Solution().singleNumber(nums = [1,1,2,2,3])
print(Output)