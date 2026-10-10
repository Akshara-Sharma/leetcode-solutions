class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        chars = list(s.split())
        i = 0
        result = ""

        while i < k:
            result += chars[i] + " "
            i += 1

        return(result.strip())
Output = Solution().truncateSentence(s = "Hello how are you Contestant", k = 4)
print(Output)