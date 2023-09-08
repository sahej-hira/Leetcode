# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def constructbst(preorder,start,end):
            if start > end:
                return None

            root = TreeNode(preorder[start])
            i = start + 1
            
            while i <= end and preorder[i] <= root.val:
                i += 1
            root.left = constructbst(preorder,start + 1, i - 1)
            root.right = constructbst(preorder, i, end)
            return root

        return constructbst(preorder,0,len(preorder) - 1)

            
            