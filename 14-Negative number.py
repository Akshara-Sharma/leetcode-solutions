class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] < 0):
                    total += 1
                else:
                    continue
        return(total)

Output = Solution().countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
print(Output)