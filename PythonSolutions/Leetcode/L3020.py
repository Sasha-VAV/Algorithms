class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ones = 0
        ref = defaultdict(lambda: defaultdict(int))

        for num in nums:
            if num == 1:
                ones += 1
                continue
            count = 1
            curr = num
            while abs(curr ** 0.5 - round(curr ** 0.5)) < 1e-6:
                count *= 2
                curr = round(curr ** 0.5)
            ref[curr][count] += 1

        res = (ones + 1) // 2
        for k, v in ref.items():
            values = sorted(v.keys(), reverse=True)
            for max_value in values:
                curr = 1
                prev = max_value / 2
                while abs(prev - (prev := round(prev))) < 1e-6 and v[prev] > 1:
                    curr += 1
                    if prev == 1:
                        break
                    prev = prev / 2
                res = max(res, curr)
        return 2 * res - 1