class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cu = {'a': -1, 'b': -1, 'c':-1}
        ans = 0

        for i, x in enumerate(s):
            cu[x] = i
            ans += min(cu.values()) + 1

        return ans