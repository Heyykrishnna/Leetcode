# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def f(node, max_val):
            if not node:
                return 0

            if node.val >= max_val:
                good = 1 
            else:
                good = 0
            nm = max(max_val, node.val)
            
            return good + f(node.left, nm) + f(node.right, nm)

        return f(root, root.val)