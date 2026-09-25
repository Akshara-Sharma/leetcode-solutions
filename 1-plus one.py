class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1

        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                return digits

        digits.insert(0, 1)
        return digits

Output = Solution().plusOne(digits = [1,2,3])
print(Output)