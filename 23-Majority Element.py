class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        length = len(nums)

        for i in set(nums):
            if nums.count(i) > length // 2:
                return i

        return -1

Output = Solution().majorityElement(nums = [3,2,3])
print(Output)