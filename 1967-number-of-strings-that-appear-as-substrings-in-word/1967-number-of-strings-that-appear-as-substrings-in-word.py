class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cu = 0
        for i in patterns:
            if i in word:
                cu += 1
            
        return cu