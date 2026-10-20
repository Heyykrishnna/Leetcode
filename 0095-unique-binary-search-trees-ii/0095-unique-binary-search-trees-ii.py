# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        
        def f(l, r):
            if l > r:
                return [None]
            
            ans = []
            for i in range(l, r + 1):
                left = f(l, i - 1)
                right = f(i + 1, r)
                for j in left:
                    for k in right:
                        ans.append(TreeNode(i, j, k))
            return ans

        return f(1, n)