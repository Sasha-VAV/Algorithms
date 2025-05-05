class Solution:
    def numOfWays(self, n: int) -> int:
        nums = dict()
        for a in 'RYG':
            for b in 'RYG':
                if a == b:
                    continue
                for c in 'RYG':
                    if c == b:
                        continue
                    nums[a+b+c] = 1
        div = 10 ** 9 + 7
        for i in range(1, n):
            new_nums = nums.copy()
            for seq in nums:
                new_nums[seq] = 0
                for a in 'RYG':
                    if a == seq[0]:
                        continue
                    for b in 'RYG':
                        if a == b or b == seq[1]:
                            continue
                        for c in 'RYG':
                            if b == c or c == seq[2]:
                                continue
                            new_nums[seq] += nums[a+b+c]
                new_nums[seq] %= div
            nums = new_nums
        return sum(nums.values()) % div


if __name__ == '__main__':
    print(Solution().numOfWays(5000))