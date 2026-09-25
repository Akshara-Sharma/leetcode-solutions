class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i = 0

        while i < len(nums):
            if target == nums[i]:
                return i
            elif target < nums[i]:
                return i
            else:
                i += 1

        return i

Output = Solution().searchInsert(nums = [1,2,3,4], target = 3)
print(Output)