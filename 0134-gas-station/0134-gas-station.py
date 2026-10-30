class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        cu = 0
        st = 0
        i = 0

        while i < n:
            cu += gas[i] - cost[i]
            if cu<0:
                st = i+1
                cu = 0
            i += 1
        return st