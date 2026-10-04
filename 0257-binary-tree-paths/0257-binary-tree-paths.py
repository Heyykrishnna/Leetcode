# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if not root:
            return []

        pa = []
        cu = []

        def f(node: TreeNode):

            cu.append(str(node.val))
            if not node.left and not node.right:
                pa.append("->".join(cu))
            else:
                if node.left:
                    f(node.left)
                if node.right:
                    f(node.right)

            cu.pop()
            
        f(root)
        return pa