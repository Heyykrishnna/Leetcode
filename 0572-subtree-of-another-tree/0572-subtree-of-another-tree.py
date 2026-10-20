# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def f(s, t):
            if not s and not t:
                return True
            if not s or not t or s.val != t.val:
                return False
            return f(s.left, t.left) and f(s.right, t.right)

        if not root:
            return False
        if f(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)