class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_gcd = max(nums)

        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        gcd = [0] * (max_gcd + 1)

        for i in range(max_gcd, 0, -1):
            count = 0
            for j in range(i, max_gcd + 1, i):
                count += counter[j]
            
            gcd[i] = count * (count - 1) // 2

            for j in range(2 * i, max_gcd + 1, i):
                gcd[i] -= gcd[j]
        
        prefix = [0] * (max_gcd + 1)
        curr = 0
        for i, g in enumerate(gcd):
            curr += g
            prefix[i] = curr
        
        res = [-1] * len(queries)
        for i, query in enumerate(queries):
            res[i] = bisect_right(prefix, query)
        
        return res