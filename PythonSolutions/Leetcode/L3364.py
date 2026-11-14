class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        i = 0
        res = float('inf')
        n = len(nums)
        curr = sum(nums[:l - 1])
        for i in range(l - 1, n):
            tmp = curr
            for j in range(r - l + 1):
                if i + j >= n:
                    break
                tmp += nums[i + j]
                if tmp > 0:
                    res = min(res, tmp)
            curr += nums[i]
            curr -= nums[i - l + 1]
        return res if res != float('inf') else -1


if __name__ == "__main__":
    nums = [1,2]
    l = 2
    r = 2
    print(Solution().minimumSumSubarray(nums, l, r))