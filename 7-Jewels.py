class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        i = 0
        j = 0
        for i in range(len(jewels)):
            if(jewels[i] in stones):
                j = j + stones.count(jewels[i])
                i += 1
        return(j)

Output = Solution().numJewelsInStones(jewels = "aA", stones = "aAAbbbb")
print(Output)