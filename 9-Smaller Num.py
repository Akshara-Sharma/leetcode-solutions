class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        list2 = []
        for i in range(len(nums)):
            count = 0
            num = nums[i]
            j = i + 1
            for j in range(len(nums)):
                if (num > nums[j]):
                    count += 1
            list2.append(count)

        return(list2)

Output = Solution().smallerNumbersThanCurrent(nums= [8,1,2,2,3])
print(Output)