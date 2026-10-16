class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        maximum = max(nums)
        minimum = min(nums)
        i = 0
        while i < len(nums):
            if (nums[i] == maximum or nums[i] == minimum):
                i += 1
                continue
            else:
                return(nums[i])
            break
        if (len(nums) == 2 or len(nums) == 1):
            return(-1)

Output = Solution().findNonMinOrMax(nums = [3,2,1,4])
print(Output)