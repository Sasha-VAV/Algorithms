class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = n ** 2
        sum_even = sum_odd + n
        return gcd(sum_odd, sum_even)