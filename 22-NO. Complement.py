class Solution:
    def findComplement(self, num: int) -> int:
        binary = str(bin(num)[2:])
        result = ""

        for digit in binary:
            if digit == "1":
                result += "0"
            else:
                result += "1"

        decimal = int(result,2)
        return(decimal)

Output = Solution().findComplement(num = 5)
print(Output)