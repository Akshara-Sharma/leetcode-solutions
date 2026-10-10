class Solution:
    def sumOfMultiples(self, n: int) -> int:
        i = 1
        sum = 0
        while i < (n+1):
            if(i % 3 == 0):
                sum += i
                i += 1
            elif(i % 5 == 0):
                sum += i
                i += 1
            elif(i % 7 == 0):
                sum += i
                i += 1
            else:
                i += 1
                continue
        return(sum)
Output = Solution().sumOfMultiples(n = 7)
print(Output)