class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums + nums
        return ans

Output = Solution().getConcatenation(nums= [1,2,1])
print(Output)