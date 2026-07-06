class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        curr_l, curr_r = 0, 0
        res = len(intervals)
        for l, r in intervals:
            if l >= curr_l and r <= curr_r:
                res -= 1
                continue
            curr_l = l
            curr_r = r
        return res 