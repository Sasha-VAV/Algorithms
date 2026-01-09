from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[None] * len(nums2) for _ in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                best_option = nums1[i] * nums2[j]
                if i > 0:
                    best_option = max(best_option, dp[i-1][j])
                if j > 0:
                    best_option = max(best_option, dp[i][j-1])
                if i > 0 and j > 0:
                    best_option = max(best_option, dp[i-1][j-1] + nums1[i] * nums2[j])
                dp[i][j] = best_option
        return dp[-1][-1]


if __name__ == '__main__':
    arr1 = [-5,3,-5,-3,1]
    arr2 = [-2,4,2,5,-5]
    print(Solution().maxDotProduct(arr1, arr2))