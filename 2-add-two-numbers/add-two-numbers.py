# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a new linked list to return

        dummy = ListNode()
        head = dummy

        carry = 0
        while l1 or l2 or carry:

            # taking values from both lists
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # addition
            val = val1 + val2 + carry 

            # value and carry..adding to the linked list
            carry = val // 10
            val = val % 10
            head.next = ListNode(val)

            # updating the pointers
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next




        

        

