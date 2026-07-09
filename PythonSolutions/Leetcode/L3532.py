class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], max_diff: int, queries: List[List[int]]) -> List[bool]:
        domains = [-1] * n
        domains[0] = 0

        for i, num in enumerate(nums):
            domains[i] = domains[i - 1] + int(num - nums[i - 1] > max_diff)
        
        res = [0] * len(queries)
        for i, (u, v) in enumerate(queries):
            res[i] = domains[u] == domains[v]
        return res
                