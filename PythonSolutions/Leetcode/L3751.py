class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for x in range(num1, num2 + 1):
            x = list(map(int, str(x)))
            for i in range(1, len(x) - 1):
                if x[i - 1] < x[i] and x[i] > x[i + 1]:
                    res += 1
                if x[i - 1] > x[i] and x[i] < x[i + 1]:
                    res += 1
        return res