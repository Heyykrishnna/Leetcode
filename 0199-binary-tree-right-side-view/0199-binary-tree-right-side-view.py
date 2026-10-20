# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        ans = []

        def f(node, d):
            if not node:
                return

            if d == len(ans):
                ans.append(node.val)
            f(node.right, d + 1)
            f(node.left, d + 1)

        f(root, 0)
        return ans