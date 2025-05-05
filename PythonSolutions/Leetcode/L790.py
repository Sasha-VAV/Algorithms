from collections import deque


class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        window = deque()
        window.append(1)
        window.append(2)
        window.append(5)
        div = int(10**9 + 7)
        for i in range(3, n):
            window.append((window[-1] * 2 + window.popleft()) % div)
        return int(window[-1])


if __name__ == '__main__':
    print(Solution().numTilings(4))