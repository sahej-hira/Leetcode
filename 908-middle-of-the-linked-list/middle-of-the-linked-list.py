# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        #i=1
        #j=0

        while fast!=None and fast.next!=None:
            
            fast=fast.next.next
            slow=slow.next
            #i+=1
            #j+=1
            #print(i)
        return slow