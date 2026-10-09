class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        chars = list(allowed)
        count = 0
        i = 0
        while i < len(words):
            j = 0
            valid = 0
            while j < len(words[i]):
                if(words[i][j] in chars):
                    valid += 1
                    j += 1
                elif(words[i][j] not in chars):
                    valid = 0
                    break 
                
            if (valid == len(words[i]) ):
                count += 1
                i += 1
            elif(valid == 0):
                i += 1
            
        return(count)
Output = Solution().countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"])
print(Output)