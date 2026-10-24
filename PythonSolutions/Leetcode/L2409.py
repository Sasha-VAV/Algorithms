months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cum_sum = [0]
for month in months:
    cum_sum.append(cum_sum[-1] + month)

class Solution:
    def _get_days(self, date_str: str):
        month, day = map(int, date_str.split("-"))
        return day + cum_sum[month-1]

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        alice_arrival = self._get_days(arriveAlice)
        alice_departure = self._get_days(leaveAlice)
        bob_arrival = self._get_days(arriveBob)
        bob_departure = self._get_days(leaveBob)
        return max(0, min(alice_departure, bob_departure) - max(alice_arrival, bob_arrival) + 1)