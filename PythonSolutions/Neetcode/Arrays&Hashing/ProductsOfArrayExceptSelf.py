from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [1] * n
        prefixes = [1] * (n + 1)
        postfixes = [1] * (n + 1)
        for i, num in enumerate(nums):
            prefixes[i + 1] = num * prefixes[i]
        for i, num in enumerate(nums[::-1]):
            postfixes[n - i - 1] = num * postfixes[n - i]
        for i, (prefix, postfix) in enumerate(zip(prefixes[:-1], postfixes[1:])):
            products[i] = prefix * postfix
        return products


if __name__ == "__main__":
    nums = [-1,0,1,2,3]
    print(Solution().productExceptSelf(nums))

