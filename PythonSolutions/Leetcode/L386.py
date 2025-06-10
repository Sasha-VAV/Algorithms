from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(x):
            if x > n:
                return
            res.append(x)
            for i in range(10):
                if x == 0 and i == 0:
                    continue
                dfs(x * 10 + i)
        dfs(0)
        return res[1:]


if __name__ == '__main__':
    print(Solution().lexicalOrder(13))
