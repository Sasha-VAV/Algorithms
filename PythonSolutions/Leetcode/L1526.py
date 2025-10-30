from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = target[0]
        for t1, t2 in zip(target, target[1:]):
            x = t2 - t1
            if x > 0: res += x
        return res


if __name__ == '__main__':
    arr = [1, 2, 3, 2, 1]
    print(Solution().minNumberOperations(arr))