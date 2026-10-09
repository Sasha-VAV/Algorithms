class Solution:
    def minInsertions(self, s: str) -> int:
        balance = 0
        prev = 0
        res = 0
        for c in s:
            if c == "(":
                if prev > 0:
                    res += prev
                    prev = 0
                    if balance > 0:
                        balance -= 1
                    else:
                        res += 1
                balance += 1
            else:
                prev += 1
                if prev == 2:
                    balance -= 1
                    prev = 0
                if balance < 0:
                    res += 1
                    balance = 0
        if balance > 0:
            return balance * 2 + res - prev
        return res + prev * 2