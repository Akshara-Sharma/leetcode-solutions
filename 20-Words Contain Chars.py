class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        list = []
        i = 0
        while i < len(words):
            j = 0
            while j< len(words[i]):
                if(words[i][j] != x):
                    j += 1
                else:
                    list.append(i)
                    break
            i += 1
        return(list)

Output = Solution().findWordsContaining(words = ["leet","code"], x = "e")
print(Output)