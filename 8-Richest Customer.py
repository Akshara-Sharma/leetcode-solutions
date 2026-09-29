class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        i = 0
        j = 0
        nums = []
        for i in range(len(accounts)):
            num = 0

            for j in range(len(accounts[i])):
                num = num + accounts[i][j]
            nums.append(num)

        return(max(nums))

Output = Solution().maximumWealth(accounts= [[1,2,3],[3,2,1]])
print(Output)