from collections import Counter
import math


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        start = 10 ** (n // 2 - 1)
        finish = int(start * 10)
        start = 0 if start < 1 else start
        combinations = set()
        count = 0
        def hash_counter(counter):
            res = [0] * 10
            for k, v in counter.items():
                res[int(k)] = int(v)
            ans = ""
            for i, x in enumerate(res):
                ans += f"|[{i}]{x}"
            return ans
        def add_new_nums(string):
            nonlocal count
            nonlocal combinations
            if int(string) % k != 0:
                return
            c = Counter(string)
            hashed_c = hash_counter(c)
            if hashed_c not in combinations:
                tmp = n - c.get("0", 0)
                tmp *= math.factorial(n - 1)
                for i in range(10):
                    tmp //= math.factorial(c.get(str(i), 0))
                count += tmp
                combinations.add(hashed_c)
        for x in range(start, finish):
            s = str(x) if x > 0 else ""
            if n % 2 == 1:
                for j in range(10):
                    tmp_x = s + str(j) + s[::-1]
                    add_new_nums(tmp_x)
            else:
                add_new_nums(s + s[::-1])
        return count


if __name__ == '__main__':
    n = 8
    k = 1
    print(Solution().countGoodIntegers(n, k))