class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count = 0

        for word in words:
            if word.startswith(pref):
                count +=  1
            else:
                continue
        return(count)

Output = Solution().prefixCount(words = ["pay","attention","practice","attend"], pref = "at")
print(Output)