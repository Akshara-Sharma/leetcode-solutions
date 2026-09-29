class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        word3 = ""
        word4 = ""

        for i in range(len(word1)):
            word3 = word3 + word1[i]

        for j in range(len(word2)):
            word4 = word4 + word2[j]

        if (word3 == word4):
            return(True)
        else:
            return(False)

Output = Solution().arrayStringsAreEqual(word1= ["ab", "c"] , word2= ["a", "bc"])
print(Output)