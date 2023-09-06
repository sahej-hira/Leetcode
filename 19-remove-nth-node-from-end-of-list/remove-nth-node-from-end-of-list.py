# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node
        # identify l and r positioning
        # traverse thru with and without l:
        # modify where necessary

        dummy = ListNode(0,head)

        left = dummy
        right= head

        while n > 0 and right != None:
            right = right.next
            n -= 1

        while right != None:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next




        '''
            # reverse list , itr and return 
            # one pass solution

            if not head or not head.next:
                return head

            temp = head
            nhead = head.next

            while temp.next != None:
                
                temp.next = temp.next.next
                nhead.next = head

    ###########################
                head = nhead
                nhead = temp.next
                
                
            i = 0
            temp = 
            while i < n:
                if i 
            return head

        '''
        