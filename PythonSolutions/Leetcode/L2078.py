class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # Since the constraints are too small I'm using the brute-force solution
        # But it could be solved with 2 pointers more optimally
        res = 0
        n = len(colors)
        for i, c in enumerate(colors):
            for j in range(n - 1, i + res, -1):
                if colors[j] != c:
                    res = j - i
                    break
        return res