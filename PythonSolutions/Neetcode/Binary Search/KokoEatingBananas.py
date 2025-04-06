from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_speed = right
        while left <= right:
            mid = (left + right) // 2
            tmp = 0
            for pile in piles:
                tmp += pile // mid + (pile % mid > 0)
            if tmp > h:
                left = mid + 1
            else:
                min_speed = min(min_speed, mid)
                right = mid - 1
        return min_speed


if __name__ == '__main__':
    piles = [3, 6, 7, 11]
    h = 8
    print(Solution().minEatingSpeed(piles, h))
