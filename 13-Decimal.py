class Solution:
    def removeZeros(self, n: int) -> int:
        num = str(n)
        result = ""
        for digit in num:
            if (digit == "0"):
                continue
            else:
                result += digit

        return(int(result))

Output = Solution().removeZeros(n = 1020030)
print(Output)