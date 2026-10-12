class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count1 = (high + 1) // 2
        count2 = low // 2
        return(count1 - count2)

Output = Solution().countOdds(low = 3, high = 7)
print(Output)