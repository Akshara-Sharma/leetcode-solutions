class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged = sorted(nums1[:m] + nums2)
        nums1[:] = merged

Output = Solution().merge(nums1= [1,2,3,0,0] , m= 3 , nums2= [2,3,5] , n= 3)
print(Output)