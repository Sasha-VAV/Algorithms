class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = dict()
        k = len(arr) // 4 + 1
        for x in arr:
            counts[x] = counts.get(x, 0) + 1
            if counts[x] == k:
                return x