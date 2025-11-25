class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        visited = set()
        curr = 0
        while curr not in visited:
            visited.add(curr)
            curr = (curr * 10 + 1) % k
        return len(visited) if curr == 0 else -1


if __name__ == '__main__':
    print(Solution().smallestRepunitDivByK(1))