class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cu = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for i in text:
            if i in cu:
                cu[i] += 1
            
        return min(
            cu['b'], cu['a'], cu['l'] // 2, cu['o'] // 2, cu['n']
        )