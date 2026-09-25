class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

Output = Solution().strStr(haystack= "leetcode", needle= "leeto")
print(Output)