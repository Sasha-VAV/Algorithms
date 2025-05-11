class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        q = deque()
        for x in arr:
            if x % 2 == 1:
                q.append(x)
                if len(q) == 3:
                    return True
                continue
            q.clear()
        return False