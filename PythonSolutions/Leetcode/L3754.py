class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        x_sum = 0
        for num in map(int, str(n)):
            if num == 0:
                continue
            x *= 10
            x += num
            x_sum += num
        return x_sum * x