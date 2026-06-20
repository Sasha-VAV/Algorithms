class Solution:
    def processStr(self, s: str, k: int) -> str:
        curr_len = 0
        for c in s:
            match c:
                case "*":
                    if curr_len > 0:
                        curr_len -= 1
                case "#":
                    curr_len *= 2
                case "%":
                    pass
                case _:
                    curr_len += 1
        if not (0 <= k < curr_len):
            return "."
        
        for c in reversed(s):
            match c:
                case "*":
                    # Here might be error
                    curr_len += 1
                case "#":
                    if curr_len % 2 != 0:
                        raise ValueError(f"{curr_len=}")
                    curr_len //= 2
                    k %= curr_len
                case "%":
                    k = curr_len - k - 1
                case _:
                    curr_len -= 1
                    if k == curr_len:
                        return c
        raise ValueError("Something went wrong")
        
        