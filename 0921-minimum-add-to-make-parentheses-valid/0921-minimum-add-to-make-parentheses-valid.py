class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ope = add = 0

        for i in s:
            if i == '(':
                ope += 1
            else:
                if ope > 0:
                    ope -= 1
                else:
                    add += 1
                
        return ope + add