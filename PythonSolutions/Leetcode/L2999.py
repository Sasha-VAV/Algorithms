import math


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        suffix = len(s)
        if int(suffix) > finish:
            return 0
        for c in s:
            if int(c) > limit:
                return 0
        bias = int(int(suffix) >= start)
        start //= int(math.pow(10, suffix))
        finish //= int(math.pow(10, suffix))
        s_start = str(start)
        s_finish = str(finish)
        first_digit = int(min(int(s_finish[0]), limit)) - int(s_start[0]) if len(s_start) == len(s_finish) else 1
        if finish - start < 10:
            return first_digit + bias
        bias -= int(s_start[0])
        other_digits = int(math.pow(limit, math.ceil(math.log10(finish - start))))
        return first_digit * other_digits + bias


if __name__ == '__main__':
    start = 1
    finish = 60000
    limit = 4
    s = "123"
    print(Solution().numberOfPowerfulInt(start, finish, limit, s))