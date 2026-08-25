class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        max_number = 100
        counts = [0] * (max_number // k)

        for num in nums:
            if num % k == 0:
                counts[num // k - 1] += 1

        for i, count in enumerate(counts):
            if count == 0:
                return (i + 1) * k
        return (len(counts) + 1) * k 