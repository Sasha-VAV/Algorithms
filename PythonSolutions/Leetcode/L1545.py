class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        curr = False
        curr_len = 2 ** n - 1
        while n > 1:
            if k == curr_len // 2 + 1:
                return "0" if curr else "1"
            if k > curr_len // 2 + 1:
                curr = not curr
                k = curr_len - k + 1
            n -= 1
            curr_len -= curr_len // 2 + 1
        return "1" if curr else "0"


if __name__ == "__main__":
    print(Solution().findKthBit(4, 11))
    # 123456789012345