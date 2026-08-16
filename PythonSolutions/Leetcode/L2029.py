class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        counts = [0] * 3
        for stone in stones:
            counts[stone % 3] += 1
        
        if counts[0] % 2:
            return abs(counts[1] - counts[2]) > 2
        
        return bool(counts[1] and counts[2])
        
        