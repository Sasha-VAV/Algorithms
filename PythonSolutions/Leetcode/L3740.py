class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        occurences = defaultdict(list)
        for i, num in enumerate(nums):
            occurences[num].append(i)
        
        res = None
        for v in occurences.values():
            for i in range(len(v) - 2):
                r = 2 * v[i + 2] - 2  * v[i]               
                if res is None:
                    res = r
                else:
                    res = min(res, r)
        return -1 if res is None else res