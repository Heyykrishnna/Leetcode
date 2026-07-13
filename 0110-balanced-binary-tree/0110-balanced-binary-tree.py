# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def f(node):
            if not node:
                return [True, 0]
            
            leb, leh = f(node.left)
            rib, rih = f(node.right)

            ans = leb and rib and (abs(leh - rih) <= 1)
            return [ans, 1 + max(leh, rih)]
        
        return f(root)[0]