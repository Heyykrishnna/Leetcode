class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        pre = {0: 1}
        bal = vc = ans = 0
        
        for x in nums:
            if x == target:
                bal += 1
                vc += pre.get(bal - 1, 0)
            else:
                bal -= 1
                vc -= pre.get(bal, 0)
                
            pre[bal] = pre.get(bal, 0) + 1
            ans += vc
            
        return ans