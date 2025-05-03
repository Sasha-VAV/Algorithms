from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        vals = dict()
        vals[tops[0]] = (0, 0 if tops[0] == bottoms[0] else 1)
        if bottoms[0] != tops[0]: vals[bottoms[0]] = (1, 0)
        for t, b in zip(tops[1:], bottoms[1:]):
            c1 = t in vals
            c2 = b in vals
            if not c1 and not c2:
                return -1
            if t == b:
                if len(vals) == 1:
                    continue
                a = vals[t]
                vals.clear()
                vals[b] = a
                continue
            if not c1:
                a = vals[b]
                vals.clear()
                vals[b] = (a[0]+1, a[1])
                continue
            if not c2:
                a = vals[t]
                vals.clear()
                vals[t] = (a[0], a[1]+1)
                continue
            a = vals[t]
            vals[t] = (a[0], a[1] + 1)
            a = vals[b]
            vals[b] = (a[0] + 1, a[1])
        if not vals:
            return -1
        return min([min(a,b) for a, b in vals.values()])


if __name__ == '__main__':
    tops = [2,1,2,4,2,2]
    bottoms = [5,2,6,2,3,2]
    print(Solution().minDominoRotations(tops, bottoms))