class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        list = []
        for i in range(n+1):
            list.append(i)
        for j in range(len(list)):
            if (list[j] in nums):
                pass
            else:
                return(list[j])

Output = Solution().missingNumber(nums= [3,0,1])
print(Output)