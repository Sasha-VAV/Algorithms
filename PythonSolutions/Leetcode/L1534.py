from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i, x in enumerate(arr):
            for j, y in enumerate(arr[i+1:]):
                for k, z in enumerate(arr[i+j+2:]):
                    if abs(x-y) <= a and abs(x-z) <= c and abs(y-z) <= b:
                        count += 1
        return count


if __name__ == '__main__':
    arr = [3,0,1,1,9,7]
    a = 7
    b = 2
    c = 3
    print(Solution().countGoodTriplets(arr, a, b, c))