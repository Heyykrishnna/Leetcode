class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        d = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def f(s):
            return sum(d[:int(s[:2])]) + int(s[3:])
            
        a = max(arriveAlice, arriveBob)
        b = min(leaveAlice, leaveBob)
        
        return max(0, f(b) - f(a) + 1)