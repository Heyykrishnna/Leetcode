class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []

        for i in words:
            su = 0
            for j in i:
                su += weights[ord(j) - ord('a')]
            
            va = su % 26
            ans.append(chr(ord('z') - va))
        
        return ''.join(ans)