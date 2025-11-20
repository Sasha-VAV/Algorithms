from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[1], x[0]))
        res = 0
        prev = [-2, -1]
        for a, b in intervals:
            if prev[0] < a:
                prev[0] = prev[1] if prev[1] < b else b - 1
                prev[1] = b
                res += 1
            if prev[0] < a:
                prev[0] = b - 1
                res += 1
        return res


if __name__ == '__main__':
    arr = [[1,3],[3,7],[5,7],[7,8]]
    print(Solution().intersectionSizeTwo(arr))