class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ans = []
        nums1 = sorted(nums)
        for i in range(len(nums1)):
            if (nums1[i] == target):
                ans.append(i)
            else:
                continue
        return(ans)
Output = Solution().targetIndices(nums = [1,2,5,2,3], target = 2)
print(Output)