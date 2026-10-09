class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = s.count(s[0])
        i = 0
        while i < len(s):
            if s.count(s[i]) != count :
                return(False)
                break
            else:
                i += 1
        else:
            return(True)
Output = Solution().areOccurrencesEqual(s = "abacbc")
print(Output)