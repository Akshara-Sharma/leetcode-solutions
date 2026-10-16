class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = [int(digit) for digit in str(num)]
        result = ""
        flag = False
        i = 0
        while (i < len(digits)):
            if(digits[i] == 9):
                result += (str(digits[i]))
                i += 1
            elif(digits[i] == 6 and flag == False):
                result += ("9")
                i += 1
                flag = True  
            elif(digits[i] == 6 and flag == True):
                result += str(digits[i])
                i += 1
            else:
                result += str(digits[i])
                i += 1
        return(int(result))

Output = Solution().maximum69Number(num = 9669)
print(Output)