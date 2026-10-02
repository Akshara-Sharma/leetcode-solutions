class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        result = set()

        for num in nums:
            if num in result:
                return(True)
            else:
                result.add(num)
        else:
            return(False)

Output = Solution().containsDuplicate(nums= [1,2,3,1])
print(Output)