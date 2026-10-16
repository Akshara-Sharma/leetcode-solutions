class Solution:
    def isPalindrome(self, s: str) -> bool:
        Alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        str1 = ""
        str2= ""
        for char in s:
            if char.isalnum():
                str1 += char.lower()
            else:
                continue
        str2 = str1[::-1]
        if(str1 == str2):
            return(True)
        else:
            return(False)
        
Output  = Solution().isPalindrome(s = "A man, a plan, a canal: Panama")
print(Output)