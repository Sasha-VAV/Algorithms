from collections import deque


FACTORIZATION = defaultdict(list)
for i in range(2, 1_000_001):
    for j in range(i, 1_000_001, i):
        FACTORIZATION[j].append(i)

class Solution:
    def minJumps(self, nums: list[int]) -> int:
        edges = defaultdict(list)
        for i, x in enumerate(nums):
            for y in FACTORIZATION[x]:
                edges[y].append(i)
        q = deque()
        q.appendleft(0)
        seen = {0}
        res = 0
        n = len(nums) - 1
        while q:
            new_q = deque()
            while q:
                i = q.pop()
                x = nums[i]
                if i == n:
                    return res
                candidates = [i - 1, i + 1]
                if len(FACTORIZATION[x]) == 1:
                    for j in edges[x]:
                        if j not in seen:
                            candidates.append(j)
                    edges[x].clear()
                for i in candidates:
                    if i not in seen and 0 <= i <= n:
                        new_q.appendleft(i)
                        seen.add(i)
            q = new_q
            res += 1
        return res


if __name__ == "__main__":
    nums = [1,2,4,6]
    print(Solution().minJumps(nums))