class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        list = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    list.append(nums1[i])
                else:
                    pass

        result = []

        for num in list:
            if num not in result:
                result.append(num)

        return result

Output = Solution().intersection(nums1 = [1,2,2,1], nums2 = [2,2])
print(Output)