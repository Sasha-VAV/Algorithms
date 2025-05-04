class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        n = len(firstList)
        m = len(secondList)
        res = []
        while i < n and j < m:
            a1, b1 = firstList[i]
            a2, b2 = secondList[j]
            a = max(a1, a2)
            b = min(b1, b2)
            if a <= b:
                res.append([a, b])
            if b1 < b2:
                i += 1
            else:
                j += 1
        return res