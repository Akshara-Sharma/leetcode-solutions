class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            if len(s) != len(t):
                return(False)
            elif s.count(char) != t.count(char):
                return(False)
                break
        else:
            return(True)

Output = Solution().isAnagram(s = "anagram", t = "nagaram")
print(Output)