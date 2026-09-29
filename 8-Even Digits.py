class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        length = 0
        for i in range(len(nums)):
            length = len(str(nums[i]))
            if length % 2 == 0:
                count += 1
        return(count)

Output = Solution().findNumbers(nums= [12,345,2,6,7896])
print(Output)