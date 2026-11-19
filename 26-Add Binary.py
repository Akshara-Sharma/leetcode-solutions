class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)

        result = num1 + num2

        binary = bin(result)[2:]

        return(binary) 

Output = Solution().addBinary(a = "11", b = "1")
print(Output)