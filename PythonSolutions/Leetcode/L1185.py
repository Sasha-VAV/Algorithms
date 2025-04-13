class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day -= 1
        month -= 1
        year -= 1970
        extra_days = (year + 1) // 4
        days = year * 365 + extra_days
        d_31 = [1, 3, 5, 7, 8, 10, 12]
        d_30 = [4, 6, 9, 11]
        for i in range(1, month+1):
            if i in d_31:
                days += 31
            elif i in d_30:
                days += 30
            else:
                days += 28 + int(
                    (year + 2) % 4 == 0 and ((year + 1970) % 100 != 0 or (year + 1970) % 400 == 0))
        days += day
        dow = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return dow[(days + 4) % 7]


if __name__ == '__main__':
    print(Solution().dayOfTheWeek(31, 8, 2100))