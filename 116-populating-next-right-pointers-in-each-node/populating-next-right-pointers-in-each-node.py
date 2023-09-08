"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return root
        cur, nxt_level = root,root.left

        while cur and nxt_level:
            #connecting
            cur.left.next = cur.right
            if cur.next:        #exists
                cur.right.next = cur.next.left
            

            #shifting 
            
            if cur.next == None:
                cur = nxt_level
                nxt_level = nxt_level.left
            else:
                cur = cur.next
            
        return root





        '''
        if not root and not root.left :
            return root
        root.next = root.right
        if root.right != None:
            root.right.next = root.left
        else:   #root.right == None(rhs)
            root.next = None
        self.connect(root.left)
        self.connect(root.right)
        '''

        