class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        for i, d in enumerate(digits[::-1]):
            if d == 9:
                digits[n - i] = 0
                continue
            digits[n - i] += 1
            return digits
        return [1] + digits