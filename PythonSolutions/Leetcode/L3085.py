from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)
        arr = list(counter.values())
        arr.sort()
        n = len(arr)
        prefix = [0]
        for x in arr:
            prefix.append(prefix[-1] + x)
        res = prefix[-1]
        i = 0
        j = 0
        while j < n:
            if arr[j] - arr[i] <= k:
                j += 1
            else:
                if arr[j - 1] - arr[i] <= k:
                    x = prefix[i] + max(prefix[-1] - prefix[j] - (arr[i] + k) * (n - j), 0)
                    res = min(res, x)
                i += 1
                j = max(i, j)
        else:
            if arr[j - 1] - arr[i] <= k:
                x = prefix[i] + max(prefix[-1] - prefix[j] - (arr[i] + k) * (n - j), 0)
                res = min(res, x)
        return res


if __name__ == '__main__':
    word = "dabdcbdcdcd"
    k = 2
    print(Solution().minimumDeletions(word, k))