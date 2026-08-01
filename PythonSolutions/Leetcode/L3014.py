class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        curr_cost = 0
        remaining = 0
        res = 0

        for _, count in counter.most_common():
            if not remaining:
                curr_cost += 1
                remaining = 8

            res += curr_cost * count
            remaining -= 1
        return res