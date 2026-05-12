class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks = sorted(tasks, key=lambda x: -(x[1] - x[0]))
        res = 0
        curr = 0
        for actual, minimum in tasks:
            if minimum > curr:
                res += minimum - curr
                curr = minimum
            curr -= actual
        return res