# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val >= list2.val:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2
        else:
            list1.next = self.mergeTwoLists(list1.next,list2) 
            return list1
        


        '''     ITERATIVE APPROACH
        # method 1: create a new linked list thru dummy node
        # method 2: in-place modification of a list with the another

        # used method 1 here
        if not list1 and not list2: # are enpty
            return list1

        
        dummy = ListNode() #dummy listnode  ~ creating new linked list
        head = dummy
        while list1 and list2: # are not empty
                        
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
                

        if list1:
            head.next = list1
        elif list2:
            head.next = list2
        return dummy.next
        '''
        

                





         
        