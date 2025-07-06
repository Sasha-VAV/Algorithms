class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        res = -1
        for k, v in counter.items():
            if k == v and k > res:
                res = k
        return res