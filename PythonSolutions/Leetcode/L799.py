class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        i = 0
        no_water_left = False
        while i < query_row and not no_water_left:
            i += 1
            next_row = [0] * (i + 1)
            no_water_left = True
            for j in range(len(row)):
                overflow = (row[j] - 1) / 2
                if overflow > 0:
                    no_water_left = False
                else:
                    continue
                next_row[j] += overflow
                next_row[j + 1] += overflow
            row = next_row
        if no_water_left:
            return 0
        return min(row[query_glass], 1)


if __name__ == '__main__':
    poured = 2
    query_row = 1
    query_glass = 1
    print(Solution().champagneTower(poured, query_row, query_glass))