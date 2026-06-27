class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cu = Counter(nums)
        ml = 0
        if 1 in cu:
            if cu[1] % 2 != 0:
                ml = cu[1]     
            else:
                ml = cu[1] - 1

        for i in cu:
            if i == 1:
                continue
                
            cl = 0
            x = i
            
            while cu[x] >= 2:
                cl += 2
                x = x*x

            if cu[x] >= 1:
                cl += 1
            else:
                cl -= 1
                
            ml = max(ml, cl)
            
        return ml