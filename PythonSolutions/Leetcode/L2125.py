class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = bank[0].count("1")
        res = 0
        for row in bank[1:]:
            tmp = row.count("1")
            if not tmp: continue
            res += prev * tmp
            prev = tmp
        return res