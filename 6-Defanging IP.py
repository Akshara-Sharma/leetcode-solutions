class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace("." , "[.]")

        return(address)

Output = Solution().defangIPaddr(address = "1.1.1.1")
print(Output)