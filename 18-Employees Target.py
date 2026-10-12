class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for i in range(len(hours)):
            if(hours[i] == target or hours[i] > target):
                count += 1
        return(count)
Output = Solution().numberOfEmployeesWhoMetTarget(hours = [0,1,2,3,4], target = 2)
print(Output)