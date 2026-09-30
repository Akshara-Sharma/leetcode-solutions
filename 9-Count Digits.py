class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        digits = [int(digit) for digit in str(num)]
        for i in range(len(digits)):
            if(num % digits[i] == 0 ):
                count += 1

        return(count)

Output = Solution().countDigits(num= 7)
print(Output)