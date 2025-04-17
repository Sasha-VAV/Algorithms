class Solution:
    def divisorGame(self, n: int) -> bool:
        res = dict()
        def check(n, is_alice=True):
            for x in range(1,n):
                if n % x != 0:
                    continue
                if not (n - x, not(is_alice)) in res:
                    a = check(n - x, not(is_alice))
                    res[(n - x, not(is_alice))] = a
                else:
                    a = res[(n - x, not (is_alice))]
                if a and is_alice:
                    return True
                if not a and not is_alice:
                    return False
            if is_alice:
                return False
            return True
        return check(n)


if __name__ == "__main__":
    print(Solution().divisorGame(4))