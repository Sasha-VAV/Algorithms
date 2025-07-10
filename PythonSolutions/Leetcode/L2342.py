class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        counter = defaultdict(list)
        for x in nums:
            y = sum(list(map(int, list(str(x)))))
            counter[y].append(x)
        for k, v in counter.items():
            if len(v) == 1: continue
            v.sort()
            res = max(res, v[-1] + v[-2])
        return res