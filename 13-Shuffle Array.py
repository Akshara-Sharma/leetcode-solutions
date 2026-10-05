class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        part1 = nums[:n]
        part2 = nums[n:]
        flag = 0
        result = []
        i , j = 0 , 0
        while (i < len(part1)) or (j < len(part2)):
            if (flag == 0 and i < len(part1)):
                result.append(part1[i])
                i += 1
                flag += 1
            elif(flag == 1 and j < len(part2)):
                result.append(part2[j])
                j += 1
                flag -=1
        return(result)
Output = Solution().shuffle(nums = [2,5,1,3,4,7], n = 3)
print(Output)