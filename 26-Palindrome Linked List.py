# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        str1 = ""
        current = head

        while (current is not None):
            str1 = str1 + str(current.val)
            current = current.next

        if (str1 == str1[::-1]):
            return(True)
        else:
            return(False)

Output = Solution().isPalindrome(head = [1,2,2,1])
print(Output)