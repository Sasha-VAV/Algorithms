class Solution:
    def readBinaryWatch(self, turned_on: int) -> List[str]:
        res = []
        for hour in range(12):
            hour_count = hour.bit_count()
            for minute in range(60):
                minute_count = minute.bit_count()
                if hour_count + minute_count == turned_on:
                    res.append(f"{hour}:{minute:02}")
        return res