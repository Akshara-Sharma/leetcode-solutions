class Solution:
    def arraySign(self, nums: list[int]) -> int:
        Product = 1
        for i in range(len(nums)):
            Product = Product * nums[i]
        if (Product > 0):
            return(1)
        elif(Product < 0):
            return(-1)
        else:
            return(0)

Output = Solution().arraySign(nums = [-1,-2,-3,-4,3,2,1])
print(Output)