# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, start,end):
            if not node:
                return True
            
            if not (node.val < end and node.val > start):
                return False

            return (valid(node.left,start ,node.val) and valid(node.right,node.val,end))
        return valid(root,float("-inf"),float("inf"))
        
