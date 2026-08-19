class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_seats = set(tuple(x) for x in reservedSeats)
        rows_to_check = set(x[0] for x in reserved_seats)
        res = (n - len(rows_to_check)) * 2
        for i in rows_to_check:
            pairs = [1] * 4
            for j in range(2, 10):
                if (i, j) in reserved_seats:
                    pairs[j // 2 - 1] = 0

            match sum(pairs):
                case 4:
                    res += 2
                case 3:
                    res += 1
                case 2:
                    if sum(pairs[:2]) == 2 or sum(pairs[1:3]) == 2 or sum(pairs[2:4]) == 2:
                        res += 1

        return res

