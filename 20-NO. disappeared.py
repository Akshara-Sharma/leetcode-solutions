class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        maximum = max(nums)
        minimum = min(nums)
        nums_set = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i in nums_set:
                continue
            else:
                result.append(i)

        return result

Output = Solution().findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1])
print(Output)