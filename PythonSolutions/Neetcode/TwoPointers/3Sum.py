from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = list()
        for i, num in enumerate(nums):
            j, k = i+1, len(nums)-1
            while j < k:
                if num + nums[j] + nums[k] > 0:
                    k -= 1
                elif num + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    tmp = [num, nums[j], nums[k]]
                    if tmp not in triplets:
                        triplets.append(tmp)
                    j += 1
        return triplets


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
