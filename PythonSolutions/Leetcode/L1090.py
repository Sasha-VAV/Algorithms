import heapq


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        kv = dict()
        for l, v in zip(labels, values):
            if l not in kv:
                kv[l] = []
            x = kv[l]
            if len(x) < useLimit or x[0] < v:
                heapq.heappush(x, v)
            if len(x) > useLimit:
                heapq.heappop(x)
        res = []
        val = 0
        for _, v in kv.items():
            for x in v:
                if len(res) < numWanted or res[0] < x:
                    heapq.heappush(res, x)
                    val += x
                if len(res) > numWanted:
                    val -= heapq.heappop(res)
        return val