import heapq


class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.heap = []
        heapq.heappush(self.heap, (-1, -1, n))

    def dist(self, x, y):
        if x == -1:
            return y
        if y == self.n:
            return self.n - x - 1
        return abs(y - x) // 2

    def seat(self) -> int:
        _, x, y = heapq.heappop(self.heap)
        if x == -1:
            seat = 0
        elif y == self.n:
            seat = self.n - 1
        else:
            seat = (y + x) // 2
        heapq.heappush(self.heap, (-self.dist(x, seat), x, seat))
        heapq.heappush(self.heap, (-self.dist(seat, y), seat, y))
        return seat

    def leave(self, p: int) -> None:
        head = tail = None
        for i, x in enumerate(self.heap):
            if x[1] == p:
                tail = x
            if x[2] == p:
                head = x
            if head and tail:
                break
        self.heap.remove(head)
        self.heap.remove(tail)
        heapq.heapify(self.heap)
        x = head[1]
        y = tail[2]
        heapq.heappush(self.heap, (-self.dist(x, y), x, y))


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)


if __name__ == '__main__':
    exam = ExamRoom(10)
    print(exam.seat())
    print(exam.seat())
    print(exam.seat())
    print(exam.seat())
    exam.leave(4)
    pass