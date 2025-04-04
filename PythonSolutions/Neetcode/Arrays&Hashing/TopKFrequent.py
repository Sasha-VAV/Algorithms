from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        for num in nums:
            data[num] = data.get(num, 0) + 1
        sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
        items = [item[0] for item in sorted_items[:k]]
        return items


if __name__ == "__main__":
    nums = [1,2,2,3,3,3]
    print(Solution().topKFrequent(nums, 2))

