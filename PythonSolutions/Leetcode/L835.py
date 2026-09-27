from typing import List
from bisect import bisect_left


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        indices1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
        indices2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]
        if not indices1 or not indices2:
            return 0
        
        shifts = defaultdict(int)
        for x1, y1 in indices1:
            for x2, y2 in indices2:
                shifts[x1 - x2, y1 - y2] += 1
        return max(shifts.values())

if __name__ == "__main__":
    img1 = [[1,1,0],[0,1,0],[0,1,0]]
    img2 = [[0,0,0],[0,1,1],[0,0,1]]
    print(Solution().largestOverlap(img1, img2))