class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.split()[-1]
        return(len(last_word))

Output = Solution().lengthOfLastWord(s= "Hello World")
print(Output)