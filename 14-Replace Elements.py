class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        greatest = arr[-1]
        result = [-1]
        i = len(arr) - 2
        while i >= 0:
            result.append(greatest)

            if arr[i] > greatest:
                greatest = arr[i]

            i -= 1
        result.reverse()

        return(result)
Output = Solution().replaceElements(arr = [17,18,5,4,6,1])
print(Output)