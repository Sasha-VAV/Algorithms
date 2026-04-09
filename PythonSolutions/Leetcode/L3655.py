class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        t = int(n ** 0.5)
        mod = 10 ** 9 + 7
        groups = [[] for _ in range(t)]
        for l, r, k, v in queries:
            if k >= t:
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % mod
            else:
                groups[k].append((l, r, v))
        
        for k in range(1, t):
            if not groups[k]:
                continue
            diff = [1] * (n + t)
            for l, r, v in groups[k]:
                diff[l] = diff[l] * v % mod
                r = l + ((r - l) // k + 1) * k
                diff[r] = diff[r] * pow(v, mod - 2, mod) % mod
            
            for i in range(k, n):
                diff[i] = diff[i] * diff[i - k] % mod
            
            for i in range(n):
                nums[i] = nums[i] * diff[i] % mod
        
        res = 0
        for num in nums:
            res ^= num
        return res
            
