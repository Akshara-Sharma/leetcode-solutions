class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        Vowels = ["a" , "e" , "i" , "o" , "u"]
        result = 0
        i = left
        while i<= right:
            count = 0
            chars = ""
            chars += words[i][0]
            chars += words[i][len(words[i])-1]
            if (chars[0] in Vowels):
                count += 1
            if (chars[1] in Vowels):
                count+=1
            if(count == 2):
                result += 1
            i += 1
        return(result)

Output = Solution().vowelStrings(words = ["are","amy","u"], left = 0, right = 2)
print(Output)