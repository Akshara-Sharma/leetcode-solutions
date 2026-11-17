# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        current = head
        while current is not None and current.next is not None:
            if(current.val == current.next.val):
                current.next = current.next.next
            elif(current.val != current.next.val):
                current = current.next
        current = head
        while current is not None:
            return(current)
            current = current.next

Output = Solution().deleteDuplicates(head = [1,1,2])
print(Output)