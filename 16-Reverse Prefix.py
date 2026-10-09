class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        chars = list(word)
        result = ""
        str1 = ""
        str2 = ""
        n = len(chars)
        for i in range(len(chars)):
            if (chars[i] == ch):
                list1 = chars[0:i+1]
                list2 = chars[i+1:n]
                list1.reverse()
                for j in range(len(list1)):
                    str1 += list1[j]
                for k in range(len(list2)):
                    str2 += list2[k]
                result = str1 + str2
                return(result)
                break
        else:
            return(word)
Output = Solution().reversePrefix(word = "abcdefd", ch = "d")
print(Output)