from collections import Counter


class Solution:
    def specialArray(self, nums: list[int]) -> int:
        counter = Counter(nums)
        curr = 0
        query = -1
        for k, v in sorted(counter.items(), key=lambda x: -x[0]):
            curr += v
            if k < query: 
                return query
            if k < curr:
                return -1
            if k == curr:
                return k
            query = curr
        return query


if __name__ == "__main__":
    nums = [3,5]
    print(Solution().specialArray(nums=nums))