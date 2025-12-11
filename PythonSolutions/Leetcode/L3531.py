class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)
        def maintain_arr(arr, val):
            arr.append(val)
            arr.sort()
            if len(arr) == 3:
                arr[1] = arr[-1]
                arr.pop()
        res = 0
        for x, y in buildings:
            maintain_arr(rows[x], y)
            maintain_arr(cols[y], x)
        for x, y in buildings:
            if rows[x][0] < y < rows[x][-1] and cols[y][0] < x < cols[y][-1]:
                res += 1
        return res