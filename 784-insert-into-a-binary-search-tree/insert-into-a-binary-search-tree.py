# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # recursive approach 

        # base condition:
        if not root:            # if head is null
            root = TreeNode()
            root.val = val
            #root.left,root.right = None,None
            return root

        # Recursive condition
        if val >= root.val:        # if head is not null:
            root.right = self.insertIntoBST(root.right,val)
            
        else:
            root.left =  self.insertIntoBST(root.left,val)
            
        return root
        


        