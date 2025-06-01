class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(min(n, 2 * limit + 1) + 1):
            if i + limit >= n:
                res += i if i - limit <= 0 else 2 * limit - i
                res += 1
        return res


if __name__ == '__main__':
    print(Solution().distributeCandies(5, 2))