import math


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        suffix = len(s)
        finish -= int(s)
        if int(suffix) > finish or start > finish:
            return 0
        for c in s:
            if int(c) > limit:
                return 0
        bias = int(int(s) >= start)
        start //= int(math.pow(10, suffix))
        finish //= int(math.pow(10, suffix))
        s_start = str(start)
        s_finish = str(finish)
        if int(s_finish[0]) <= limit:
            res = int(s_finish[0]) * int(math.pow(limit + 1, len(s_finish) - 1))
            res += bias - 1
            tmp = 1
            for c in s_finish[1:]:
                tmp *= (min(    int(c), limit) + 1)
            res += tmp
        else:
            res = int(math.pow(limit + 1, len(s_finish)))
        tmp = 1
        for c in s_start:
            tmp *= (min(int(c), limit) + 1)
        res -= tmp - 1
        return res



if __name__ == '__main__':
    start = 1
    finish = 2000
    limit = 8
    s = "1"
    print(Solution().numberOfPowerfulInt(start, finish, limit, s))