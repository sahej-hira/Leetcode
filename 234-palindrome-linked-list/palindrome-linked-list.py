# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # method 1:creating array of the whole linked list and checking if it is a palindrome or not with a two pointer approach!

        # method 2:using fast and slow pointer approach , to reach the middle, then reversing the list and matching from the beginning and middle of the linked list!
        # fast and slow pointer approach
        slow,fast = head,head
        
        # reaching middle of the linked list and ending
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reversing second half of linked list
        prev = None

        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        ''' reversing a linked list my way:
        temp = slow
        nhead = slow.next

        while slow and slow.next:
            temp.next = temp.next.next
            nhead.next = slow

            slow = nhead 
            nhead = temp.next
        '''


        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


        



        while slow and slow.next:
            print("hau-a")
            slow = slow.next
            if slow.val != arr[::-1]:
                print(slow.val, arr[::-1])
                return False

        return True


        