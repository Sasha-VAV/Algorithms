class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = defaultdict(int)
        used_numbers = []
        for x, y in zip(nums1, nums2):
            diff = abs(x - y)
            diffs[diff] += 1
            if diffs[diff] == 1:
                heapq.heappush(used_numbers, -diff)
        
        while k and used_numbers:
            max_number = -heapq.heappop(used_numbers)
            if used_numbers:
                next_number = -used_numbers[0]
            else:
                next_number = 0
            count = diffs[max_number]
            if k >= count * (max_number - next_number):
                diffs[next_number] += count
                diffs[max_number] -= count
                k -= count * (max_number - next_number)
            else:
                level_shift, left_out = divmod(k, count)
                next_number = max_number - level_shift
                diffs[next_number] += count
                diffs[max_number] -= count
                if next_number > 0:
                    diffs[next_number - 1] += left_out
                    diffs[next_number] -= left_out
                    heapq.heappush(used_numbers, -(next_number - 1))
                heapq.heappush(used_numbers, -next_number)

                k = 0

        res = 0
        while used_numbers:
            number = -heapq.heappop(used_numbers)
            count = diffs[number]
            diffs[number] = 0
            res += number ** 2 * count
        