class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        ref = []

        for x, y in points:
            if y == 0:
                ref.append(x)
            elif x == side:
                ref.append(side + y)
            elif y == side:
                ref.append(3 * side - x)
            else:
                ref.append(4 * side - y)
        
        ref.sort()
        
        def fit_possible(limit: int):
            for start in ref:
                end = start + side * 4 - limit
                count = 0
                curr = start
                for _ in range(k - 1):
                    idx = bisect_left(ref, curr + limit)
                    if idx == len(ref) or ref[idx] > end:
                        break
                    curr = ref[idx]
                else:
                    return True
            return False
        
        l = 1
        r = side
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if fit_possible(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res