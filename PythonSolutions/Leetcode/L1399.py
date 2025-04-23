from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        counts = dict()
        for i in range(1,n+1):
            k = sum(map(int, list(str(i))))
            counts[k] = counts.get(k, 0) + 1
        counter = Counter(counts.values())
        return counter[max(counter.keys())]


if __name__ == '__main__':
    print(Solution().countLargestGroup(13))