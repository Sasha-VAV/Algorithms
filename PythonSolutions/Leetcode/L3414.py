class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals = [(r, l, weight, i) for i, (l, r, weight) in enumerate(intervals)]
        intervals.sort(key=lambda x: x[0])

        dp = [[(0, []) for _ in range(5)] for _ in range(len(intervals) + 1)]

        for i, (r, l, weight, idx) in enumerate(intervals):
            k = bisect_left(intervals, (l, ), hi=i)

            for j in range(1, 5):
                prev_weight, prev_indices = dp[k][j - 1]

                skip = dp[i][j]

                curr_weight = prev_weight - weight
                curr_indices = sorted(prev_indices + [idx])
                
                take = (curr_weight, curr_indices)

                dp[i + 1][j] = min(skip, take)
        return dp[-1][4][1]