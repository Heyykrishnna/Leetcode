class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        cu = []
        n = len(nums)
        vis = [False] * n

        def f(i):
            if i == n:
                ans.append(cu[:])
                return
            
            for j in range(n):
                if not vis[j]:
                    vis[j] = True
                    cu.append(nums[j])
                    f(i+1)
                    cu.pop()
                    vis[j] = False
                
        f(0)
        return ans