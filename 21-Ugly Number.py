
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        factors = [2, 3, 5]

        for factor in factors:
            while n % factor == 0:
                n = n // factor

        if n == 1:
            return True
        else:
            return False

Output = Solution().isUgly(n = 6)
print(Output)