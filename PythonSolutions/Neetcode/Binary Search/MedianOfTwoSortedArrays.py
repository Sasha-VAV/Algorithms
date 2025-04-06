from typing import List

# O(m+n)
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         if len(nums1) < len(nums2):
#             nums1, nums2 = nums2, nums1
#         i = 0
#         j = 0
#         median = [0] * 2
#         while i + j < (len(nums1) + len(nums2)) // 2 + 1:
#             if i == len(nums1) or j < len(nums2) and nums1[i] > nums2[j]:
#                 median.pop(0)
#                 median.append(nums2[j])
#                 j += 1
#             else:
#                 median.pop(0)
#                 median.append(nums1[i])
#                 i += 1
#         if (len(nums1) + len(nums2)) % 2 == 0:
#             return (median[0] + median[1]) / 2
#         return median[1]

# O(log(mn))
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         if len(nums1) > len(nums2):
#             nums1, nums2 = nums2, nums1
#         m, n = len(nums1), len(nums2)
#         def solve(k, a_l, b_l, a_r, b_r):
#             if a_l > a_r:
#                 return nums2[k - a_l]
#             if b_l > b_r:
#                 return nums1[k - b_l]
#             a_m = (a_l + a_r) // 2
#             b_m = (b_l + b_r) // 2
#             if a_m + b_m < k:
#                 if nums1[a_m] < nums2[b_m]:
#                     return solve(k, a_m + 1, b_l, a_r, b_r)
#                 return solve(k, a_l, b_m + 1, a_r, b_r)
#             if nums2[b_m] > nums1[a_m]:
#                 return solve(k, a_l, b_l, a_r, b_m - 1)
#             return solve(k, a_l, b_l, a_m - 1, b_r)
#         if (m + n) % 2 == 0:
#             k = (m + n) // 2 - 1
#             a = solve(k, 0, 0, m - 1, n - 1)
#             k += 1
#             b = solve(k, 0, 0, m - 1, n - 1)
#             return (a + b) / 2
#         k = (m + n) // 2
#         return solve(k, 0, 0, m - 1, n - 1)

# O(log(min(m,n)))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left <= right:
            m_a = (left + right) // 2
            m_b = (m + n + 1) // 2 - m_a
            if m_a - 1 < 0:
                max_l_a = float('-inf')
            else:
                max_l_a = nums1[m_a - 1]
            if m_a >= m:
                min_r_a = float('inf')
            else:
                min_r_a = nums1[m_a]
            if m_b - 1 < 0:
                max_l_b = float('-inf')
            else:
                max_l_b = nums2[m_b - 1]
            if m_b >= n:
                min_r_b = float('inf')
            else:
                min_r_b = nums2[m_b]
            if max_l_a > min_r_b:
                right = m_a - 1
            if max_l_b > min_r_a:
                left = m_a + 1
            if max_l_a <= min_r_b and max_l_b <= min_r_a:
                if (m + n) % 2 == 0:
                    return (max(max_l_a, max_l_b) + min(min_r_a, min_r_b)) / 2
                return max(max_l_a, max_l_b)


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [6, 7]
    print(Solution().findMedianSortedArrays(nums1, nums2))