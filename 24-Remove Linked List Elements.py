# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        
        current = head
        previous = None
        while current is not None:
            if(current.val != val):
                previous = current
                current = current.next
            elif(previous is not None):
                previous.next = current.next
                current = current.next
            elif(previous is None):
                head = current.next
                current = current.next

        return head

Output = Solution().removeElements(head = [1,2,6,3,4,5,6], val = 6)
print(Output)