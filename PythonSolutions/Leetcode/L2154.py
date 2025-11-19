class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        powers = set()
        EPS = 1e-9
        for num in nums:
            if num % original == 0:
                power = math.log2(num//original)
                if abs(power - round(power)) < EPS: powers.add(round(power))
        i = 0
        while True:
            if i not in powers: return 2 ** i * original
            i += 1
