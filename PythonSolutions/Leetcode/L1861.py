class Solution:
    def rotateTheBox(self, grid: List[List[str]]) -> List[List[str]]:
        for row in grid:
            curr = 0
            for j, x in enumerate(row):
                match x:
                    case ".":
                        continue
                    case "#":
                        curr += 1
                        row[j] = "."
                    case "*":
                        for i in range(curr):
                            row[j - i - 1] = "#"
                        curr = 0
            for i in range(curr):
                row[-i - 1] = "#"
        return list(zip(*grid[::-1]))
