class Solution:
    def subtractProductAndSum(self, n: int) -> int:
            digits = [int(digit) for digit in str(n)]
            i , Sum , Product  = 0 , 0 , 1
            while i < len(digits):
                    Product = Product * digits[i]
                    Sum = Sum + digits[i]
                    i+=1
                    Difference = Product - Sum

            return(Difference)

Output = Solution().subtractProductAndSum(n=0)
print(Output)