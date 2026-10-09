class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        final = sorted(heights)
        index = 0
        i = 0
        while i < len(heights):
            if(heights[i] == final[i]):
                i += 1
                continue
            else:
                index += 1
                i +=1
        return(index)

Output = Solution().heightChecker(heights = [1,1,4,2,1,3])
print(Output)