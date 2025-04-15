from typing import List


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        i = 1
        x_seen1 = [0] * n
        x_seen2 = [0] * n
        x_seen1[nums1[0]] = list()
        x_seen2[nums2[0]] = list()
        z_seen1 = [0] * n
        z_seen2 = [0] * n
        z_seen1[nums1[-1]] = list()
        z_seen2[nums2[-1]] = list()
        while i < n:
            x_seen1[nums1[i]] = x_seen1[nums1[i-1]] + [nums1[i-1]]
            x_seen2[nums2[i]] = x_seen2[nums2[i-1]] + [nums2[i-1]]
            z_seen1[nums1[-i - 1]] = z_seen1[nums1[-i]] + [nums1[-i]]
            z_seen2[nums2[-i - 1]] = z_seen2[nums2[-i]] + [nums2[-i]]
            i += 1
        y = 0
        for i in range(n):
            x = 0
            z = 0
            x_set = set(x_seen2[nums1[i]])
            for seen in x_seen1[nums1[i]]:
                if seen in x_set:
                    x += 1
            z_set = set(z_seen2[nums1[i]])
            for seen in z_seen1[nums1[i]]:
                if seen in z_set:
                    z += 1
            y += z * x
        return y

if __name__ == "__main__":
    arr1 = [13,14,10,2,12,3,9,11,15,8,4,7,0,6,5,1]
    arr2 = [8,7,9,5,6,14,15,10,2,11,4,13,3,12,1,0]
    print(Solution().goodTriplets(arr1, arr2))