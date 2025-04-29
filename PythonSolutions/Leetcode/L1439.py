import heapq
from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        min_sums = [0]
        for row in mat:
            new_sums = []
            for x in row:
                for val in min_sums:
                    if len(new_sums) < k or -new_sums[0] > -x+val:
                        heapq.heappush(new_sums, -x+val)
                        if len(new_sums) > k:
                            heapq.heappop(new_sums)
            min_sums = new_sums
        return -min_sums[0]


if __name__ == '__main__':
    print(Solution().kthSmallest([[1,3,11],[2,4,6]], 5))