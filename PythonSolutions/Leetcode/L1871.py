class Solution:
    def canReach(self, s: str, min_jump: int, max_jump: int) -> bool:
        visited = {0}
        q = deque([0])
        n = len(s)
        while q:
            i = q.pop()
            if i == n - 1:
                return True
            j = min(i + max_jump, n - 1)
            first_zero = None
            while j >= i + min_jump:
                if s[j] == "0" and j not in visited:
                    if first_zero is None:
                        first_zero = j
                    q.appendleft(j)
                    visited.add(j)
                    if first_zero - j >= min_jump:
                        break
                j -= 1

        return False