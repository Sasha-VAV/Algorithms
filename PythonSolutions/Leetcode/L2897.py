MODULO = 10 ** 9 + 7

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bits = [0] * 30
        res = 0
        for num in nums:
            i = 0
            while num:
                bits[i] += num & 1
                num >>= 1
                i += 1
        for _ in range(k):
            x = 0
            for i in range(len(bits)):
                if bits[i] > 0:
                    bits[i] -= 1
                    x |= 1 << i
            res += x ** 2
            res %= MODULO
        return res
                