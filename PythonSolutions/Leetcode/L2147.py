class Solution:
    def numberOfWays(self, corridor: str) -> int:
        times = [1]
        curr = 0
        mod = 10**9 + 7
        for c in corridor:
            if c == "S":
                curr += 1
                if curr == 2:
                    curr = 0
                    times.append(1)
                continue
            if curr == 0:
                times[-1] += 1
        if len(times) == 1 or curr == 1: return 0
        times[0] = 1
        times[-1] = 1
        res = 1
        for t in times:
            res *= t
            res %= mod
        return res


if __name__ == "__main__":
    string = "SSPPSPS"
    print(Solution().numberOfWays(string))