class Solution:
    def numberOfMatches(self, n: int) -> int:
        match = 0
        result = 0
        while n > 1:
            if (n % 2 != 0):
                match = ((n-1)//2)
                result += match
                n -= match
            elif(n % 2 == 0):
                match = (n//2)
                result += match
                n -= match
        return(result)
Output = Solution().numberOfMatches(n = 7)
print(Output)