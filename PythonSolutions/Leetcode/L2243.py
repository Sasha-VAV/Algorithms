from collections import deque


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        q = deque(list(map(int, s)))
        while len(q) > k:
            new_q = deque()
            curr_sum = 0
            curr_count = 0
            while q:
                curr_sum += q.popleft()
                curr_count += 1
                if curr_count == k:
                    for x in map(int, str(curr_sum)):
                        new_q.append(x)
                    curr_sum = 0
                    curr_count = 0
            if curr_count:
                for x in map(int, str(curr_sum)):
                    new_q.append(x)
            q = new_q
        return "".join(map(str, q))


if __name__ == "__main__":
    s = "1234"
    k = 2
    print(Solution().digitSum(s, k))