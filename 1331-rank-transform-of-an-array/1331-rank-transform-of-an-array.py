class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        lis = sorted(set(arr))
        rank = {}

        for i, num in enumerate(lis):
            rank[num] = i + 1
        
        return [rank[num] for num in arr]