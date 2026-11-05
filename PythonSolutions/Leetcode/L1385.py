import bisect


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        n = len(arr2) - 1
        res = 0
        for x in arr1:
            pos = bisect.bisect_left(arr2, x)
            if pos == 0 and arr2[pos] - x > d:
                res += 1
                continue
            if 0 < pos <= n and x - arr2[pos - 1] > d and arr2[pos] - x > d:
                res += 1
                continue
            if pos > n and x - arr2[n] > d:
                res += 1
        return res


if __name__ == "__main__":
    arr1 =  [2,6]
    arr2 = [-10,9,2,-1]
    d = 2
    print(Solution().findTheDistanceValue(arr1, arr2, d))