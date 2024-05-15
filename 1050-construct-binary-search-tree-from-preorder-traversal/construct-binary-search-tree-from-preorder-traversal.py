# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # preorder travesel: root left right

        # recursive case: dfs :
        
        def create(preorder, start, end):
            if start > end:
                return None     # None

            
            root = TreeNode(preorder[start])
            i = start + 1

            # all the values in the leftsubtree will be smaller than the root.val
            while i <= end  and preorder[i] < root.val:
                i += 1

            root.left = create(preorder, start + 1, i - 1)
            root.right = create(preorder, i, end)
        
            return root
            
            

        return create(preorder, 0, len(preorder) - 1)
            
        