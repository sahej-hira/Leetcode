class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Step 1: Split the list into two halves
        mid = self.getMid(head)
        left = head
        right = mid.next
        mid.next = None  # Break the link
        
        # Step 2: Recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Step 3: Merge
        return self.merge(left, right)
    
    def getMid(self, head):
        slow = head
        fast = head.next  # Important: start fast at head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, l1, l2):
        dummy = tail = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 or l2
        return dummy.next






