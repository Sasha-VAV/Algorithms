class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        rank = 0
        prev = None
        for i, x in sorted(enumerate(arr), key=lambda x: x[1]):
            if x != prev:
                rank += 1
                prev = x
            res[i] = rank
        return res