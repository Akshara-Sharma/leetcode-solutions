class Solution:
    def numberOfSteps(self, num: int) -> int:
        Step = 0
        while num != 0:
            if(num % 2 == 0):
                num = num / 2
                Step = Step + 1
            else:
                num = num - 1
                Step  = Step + 1
        return(Step)

Output = Solution().numberOfSteps(num = 14)
print(Output)