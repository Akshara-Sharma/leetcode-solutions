class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            Product = 1
            Product = nums[i] * nums[i]
            result.append(Product)
        return(sorted(result))
Output = Solution().sortedSquares(nums = [-4,-1,0,3,10])
print(Output)