class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        flag = 0
        result = ""
        i , j = 0 , 0
        while (i < len(word1)) or (j < len(word2)):
            if (flag == 0 and i < len(word1)):
                result += word1[i]
                i += 1
                flag += 1
            elif(flag == 1 and j < len(word2)):
                result += word2[j]
                j += 1
                flag -=1
            elif(j == len(word2)):
                result += word1[i]
                i +=1
            elif(i == len(word1)):
                result += word2[j]
                j +=1
            
        return(result)
Output = Solution().mergeAlternately(word1 = "abc", word2 = "pqr")
print(Output)