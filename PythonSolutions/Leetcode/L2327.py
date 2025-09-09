from collections import defaultdict


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10 ** 9 + 7
        delays = defaultdict(int)
        forgets = defaultdict(int)
        delays[1 + delay] = 1
        forgets[1 + forget] = 1
        res = 1
        curr = 0
        for i in range(2, n + 1):
            curr += delays[i] - forgets[i]
            curr %= mod
            delays[i + delay] = curr
            forgets[i + forget] = curr
            res += delays[i+delay] - forgets[i]
            res %= mod
        return res


if __name__ == '__main__':
    print(Solution().peopleAwareOfSecret(6, 2, 4))