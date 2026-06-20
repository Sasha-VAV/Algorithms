class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_degree = minutes / 60
        hour_degree = hour / 12 + minute_degree / 12
        return x if (x := abs(hour_degree - minute_degree) * 360) < 180 else 360 - x