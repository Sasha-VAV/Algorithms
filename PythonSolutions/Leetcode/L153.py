class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        res = 0
        if nums[l] < nums[r]:
            return nums[l]
        while l < r:
            mid = l + (r - l) // 2
            if nums[l] < nums[mid]:
                l = mid
                res = mid
            else:
                r = mid
        
        return nums[(res+1) % len(nums)]


if __name__ == "__main__":
    nums = [11,13,15,17]
    print(Solution().findMin(nums=nums))