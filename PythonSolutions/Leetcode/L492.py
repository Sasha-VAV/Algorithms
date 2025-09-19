class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        res = 1
        for i in range(2, int(math.sqrt(area)) + 1):
            if area % i == 0: res = i
        return [area // res, res]