from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = 2 ** len(operations)
        res = 0
        i = 0
        while k > 1:
            n //= 2
            i -= 1
            if k > n:
                k -= n
                res += operations[i]
        res %= 26
        return chr(ord('a') + res)


if __name__ == '__main__':
    k = 5
    operations = [0, 0, 0]
    print(Solution().kthCharacter(k, operations))