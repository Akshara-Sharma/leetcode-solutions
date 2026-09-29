class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        i = 0
        length = 0
        while i < len(sentences):
            if length < len(sentences[i].split()):
                length = len(sentences[i].split())
            i += 1
            
        return(length)

Output = Solution().mostWordsFound(sentences= ["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
print(Output)