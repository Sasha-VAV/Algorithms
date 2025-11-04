from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        counter = [0] * 51
        for num in nums[:k-1]:
            counter[num] += 1
        res = [0] * (len(nums) - k + 1)
        for i, num in enumerate(nums[k-1:]):
            counter[num] += 1
            tmp = [(freq, l) for l, freq in enumerate(counter) if freq]
            tmp.sort(reverse=True)
            res[i] = sum([a * b for a, b in tmp[:x]])
            counter[nums[i]] -= 1
        return res


if __name__ == '__main__':
    arr = [1,1,2,2,3,4,2,3]
    print(Solution().findXSum(arr, 6, 2))