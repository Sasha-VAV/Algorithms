class Solution:
    def checkDivisibility(self, n: int) -> bool:
        running_sum = 0
        running_mult = 1
        for x in map(int, str(n)):
            running_sum += x
            running_mult *= x
        return n % (running_sum + running_mult) == 0
