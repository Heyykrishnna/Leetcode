# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []

        def f(node):
            if not node:
                return [None]
            
            ans.append(node.val)
            f(node.left)
            f(node.right)
        
        f(root)
        return ans