class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        indices = list(range(n))
        indices.sort(key=lambda i: (sum(map(int, str(nums[i]))), nums[i]))
        graph = [0] * n
        for new_idx, old_idx in enumerate(indices):
            graph[old_idx] = new_idx
        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = graph[j]
        return n - cycles