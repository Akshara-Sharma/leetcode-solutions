class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        ans = arrivalTime + delayedTime
        ans1 = ans % 24
        if(ans1 < 10):
            return(ans1)
        else:
            return(ans1)

Output = Solution().findDelayedArrivalTime(arrivalTime = 15, delayedTime = 5)
print(Output)