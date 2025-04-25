from collections import Counter
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        res = acc = 0
        count = Counter({0: 1})
        for num in nums:
            acc = (acc + (1 if num % modulo == k else 0)) % modulo
            res += count[(acc-k) % modulo]
            count[acc] += 1
        return res


if __name__ == '__main__':
    arr = [3, 2, 4]
    print(Solution().countInterestingSubarrays(arr, 2, 1))