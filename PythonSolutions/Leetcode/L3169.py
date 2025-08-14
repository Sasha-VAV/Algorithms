from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res = meetings[0][0] - 1
        mem = meetings[0]
        for a, b in meetings[1:]:
            if mem[1] >= a:
                mem[1] = max(mem[1], b)
            else:
                res += a - mem[1] - 1
                mem = [a, b]
        return res + days - mem[1]


if __name__ == '__main__':
    days = 10
    meetings = [[5,7],[1,3],[9,10]]
    print(Solution().countDays(days, meetings))