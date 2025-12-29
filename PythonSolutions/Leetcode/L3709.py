class ExamTracker:

    def __init__(self):
        self.times = [0]
        self.prefixes = {0: 0}
        self.prev = {}


    def record(self, time: int, score: int) -> None:
        self.prefixes[time] = self.prefixes[self.times[-1]] + score
        self.prev[time] = self.times[-1]
        self.times.append(time)

    def totalScore(self, startTime: int, endTime: int) -> int:
        def bin_search(arr, x, less):
            l = 0
            r = len(arr) - 1
            res = -1
            while l <= r:
                mid = l + (r - l + 1) // 2
                if x == arr[mid]:
                    return mid
                if x > arr[mid]:
                    if less:
                        res = mid
                    l = mid + 1
                else:
                    if not less:
                        res = mid
                    r = mid - 1
            if res == -1:
                raise ValueError
            return res
        a, b = bin_search(self.times, startTime, False), bin_search(self.times, endTime, True)
        return self.prefixes[self.times[b]] - self.prefixes[self.prev[self.times[a]]]


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)

if __name__ == '__main__':
    et = ExamTracker()
    et.record(1, 98)
    print(et.totalScore(1, 1))
    et.record(5, 99)
    print(et.totalScore(1, 3))
    print(et.totalScore(1, 5))
    print(et.totalScore(3, 4))
    print(et.totalScore(2, 5))