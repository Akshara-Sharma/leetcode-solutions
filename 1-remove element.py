class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0

        while i < len(nums):
            if val == nums[i]:
                del nums[i]
            else:
                i+=1

        # print(nums)
        # k = len(nums)
        # print(k)
        return(nums)

Output = Solution().removeElement(nums = [1, 2, 3, 4], val = 3)
print(Output)