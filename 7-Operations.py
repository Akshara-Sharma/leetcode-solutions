class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        X = 0
        i = 0

        for i in range(len(operations)):
            if (operations[i] in ("--X" , "X--")):
                X = X - 1
            elif (operations[i] in ("++X" , "X++")):
                X = X + 1
            else:
                return(X)
        return(X)

Output = Solution().finalValueAfterOperations(operations= ["--X","X++","X++"])
print(Output)