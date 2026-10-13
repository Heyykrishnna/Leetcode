class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []

        def f(st, cu, tr):
            if len(cu) == k:
                if sum(cu) == n:
                    ans.append(cu[:])
                return
            
            for i in range(st, 10):
                if i > tr:
                    break
                
                cu.append(i)
                f(i+1, cu, tr - i)
                cu.pop()
        
        f(1, [], n)
        return ans