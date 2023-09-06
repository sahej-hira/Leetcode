# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # only DETECT IFF a cycle exists or NOT!
        
        slow = head
        fast = head
        #slow2 = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            #print(fast)
            if fast == slow:
                return True
            
        return False
            
        '''
        while slow2 != slow:
            print(slow)
            slow = slow.next
            fast = fast.next
        return slow2 # or slow cause they're gonna be the same!
        '''

        