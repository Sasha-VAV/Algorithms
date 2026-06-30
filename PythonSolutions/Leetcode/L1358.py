class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        curr = [0] * 3
        def transition(x):
            match x:
                case "a":
                    return 0
                case "b":
                    return 1
                case "c":
                    return 2
                case _:
                    raise ValueError(f"{x=}")
        n = len(s)
        j = 0

        res = 0
        for i, c in enumerate(s):
            while not all(curr):
                if j == n:
                    return res
                curr[transition(s[j])] += 1
                j += 1
            res += n - j + 1
            curr[transition(c)] -= 1
        return res


if __name__ == "__main__":
    s = "aaacb"
    print(Solution().numberOfSubstrings(s))