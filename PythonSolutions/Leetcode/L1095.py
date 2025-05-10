# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        arr = mountainArr
        # Find peak
        l = 1
        r = arr.length() - 2
        cache = [-1] * (r + 2)
        peak = -1
        while l <= r:
            mid = (l + r) // 2
            if cache[mid - 1] == -1: cache[mid - 1] = arr.get(mid - 1)
            if cache[mid] == -1: cache[mid] = arr.get(mid)
            if cache[mid + 1] == -1: cache[mid + 1] = arr.get(mid + 1)
            if cache[mid - 1] < cache[mid] and cache[mid] > cache[mid + 1]:
                peak = mid
                break
            if cache[mid] < cache[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
        if peak == -1:
            return -1
        l = 0
        r = peak
        while l <= r:
            mid = (l + r) // 2
            if cache[mid] == -1: cache[mid] = arr.get(mid)
            if cache[mid] == target:
                return mid
            if cache[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        l = peak
        r = arr.length() - 1
        while l <= r:
            mid = (l + r) // 2
            if cache[mid] == -1: cache[mid] = arr.get(mid)
            if cache[mid] == target:
                return mid
            if cache[mid] > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
