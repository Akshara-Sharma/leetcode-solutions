class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        num1 = max(nums)
        nums.remove(num1)
        num2 = max(nums)
        result = (num1 - 1) * (num2 - 1)
        return(result)

Output = Solution().maxProduct(nums = [3,4,5,2])
print(Output)