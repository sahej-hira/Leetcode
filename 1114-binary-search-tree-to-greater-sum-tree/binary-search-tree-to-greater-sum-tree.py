# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        addval = 0          # value to add
        def dfs(root):
            nonlocal addval
            if root:
                root.right = dfs(root.right)
                addval += root.val
                root.val = addval
                root.left = dfs(root.left)
            return root
        return dfs(root)

                


         