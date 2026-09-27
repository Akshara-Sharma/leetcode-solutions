class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()" , "o")
        command = command.replace("(al)" , "al")
        return(command)

Output = Solution().interpret(command = "G()(al)")
print(Output)