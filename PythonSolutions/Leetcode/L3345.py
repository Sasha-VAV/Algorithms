class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            # mult = reduce(lambda x, y: x * y, map(int, str(n)))
            mult = n % 10
            if n >= 10:
                mult *= n % 100 // 10
            if n >= 100:
                mult *= n % 1000 // 100
            if mult % t == 0:
                return n
            n += 1
        raise NotImplementedError("Code unreachable")