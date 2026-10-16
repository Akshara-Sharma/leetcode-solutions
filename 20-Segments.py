class Solution:
    def countSegments(self, s: str) -> int:
        return(len(s.split()))

Output = Solution().countSegments(s = "Hello, my name is John")
print(Output)