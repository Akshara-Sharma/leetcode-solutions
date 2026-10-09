class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        chars = list(s)
        n = len(chars)
        list1 = chars[0 : (n//2)]
        list2 = chars[(n//2): n]
        Vowels = ["a","e","i","o","u","A","E","I","O","U"]
        Count1 = 0
        Count2 = 0
        for i in range(len(list1)):
            if (list1[i] in Vowels):
                Count1 += 1
        for j in range(len(list2)):
            if(list2[j] in Vowels):
                Count2 += 1
        if(Count1 == Count2):
            return(True)
        else:
            return(False)
Output = Solution().halvesAreAlike(s ="book")
print(Output)