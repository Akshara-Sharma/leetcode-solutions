class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        Alphabets = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        valid = 0

        while i < len(Alphabets):
            if(Alphabets[i] in sentence):
                i += 1
                valid +=1
            else:
                return(False)
                break
        if (valid == len(Alphabets)):
            return(True)
Output = Solution().checkIfPangram(sentence = "thequickbrownfoxjumpsoverthelazydog")
print(Output)