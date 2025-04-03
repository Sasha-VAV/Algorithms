from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = dict()
        for num in nums:
            if numbers.get(num, -1) != -1:
                return True
            numbers.update({num: 1})
        return False


if __name__ == "__main__":
    arr = [1, 2, 3, 3]
    print(Solution().hasDuplicate(arr))
