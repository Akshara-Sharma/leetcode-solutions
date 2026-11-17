# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next

        count1 = (count//2) + 1
        current = head
        for i in range(count1 - 1):
            current = current.next

        return(current)

Output = Solution().middleNode(head = [1,2,3,4,5])
print(Output)