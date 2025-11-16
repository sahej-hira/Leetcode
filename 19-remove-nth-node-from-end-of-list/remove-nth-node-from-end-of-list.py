# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # no len in linked list
        # finding length
        length = 0
        c = head
        while c:
            length += 1
            c = c.next
            
        if length == n:
            return head.next   #next to next of n


        toremove = length - n
        c = head
        for _ in range(toremove - 1):# do not care about indexes
            c = c.next

        c.next = c.next.next
        return head
            
        


        
