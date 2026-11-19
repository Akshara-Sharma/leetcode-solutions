# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        str1 = ""
        current = head

        while (current is not None):
            str1 = str1 + str(current.val)
            current = current.next

        decimal = int(str1, 2)
        return(decimal)

Output = Solution().getDecimalValue(head = [1,0,1])
print(Output)