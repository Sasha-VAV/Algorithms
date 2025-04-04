from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "<$empty/>"
        return "<$string/>".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "<$empty/>":
            return []
        return s.split("<$string/>")


if __name__ == "__main__":
    strs = []
    encoded = Solution().encode(strs)
    decoded = Solution().decode(encoded)
    print(decoded)