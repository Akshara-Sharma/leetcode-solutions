class Solution:
    def firstPalindrome(self, words: list[str]) -> str:

        for word in words:

            reverse = word[::-1]

            if word == reverse:
                return word

        return ""

Output = Solution().firstPalindrome(words = ["abc","car","ada","racecar","cool"])
print(Output)