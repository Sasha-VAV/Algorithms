class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix = [float('inf')] * (n + 1)
        suffix = [float('inf')] * n
        i = 0
        curr = 0
        for j, x in enumerate(arr):
            curr += x
            while curr > target and i <= j:
                curr -= arr[i]
                i += 1
            if curr == target:
                prefix[j + 1] = min(j - i + 1, prefix[j])
        i = 0
        curr = 0
        for j, x in enumerate(reversed(arr)):
            curr += x
            while curr > target and i <= j:
                curr -= arr[-i - 1]
                i += 1
            if curr == target:
                if j == 0:
                    suffix[-j - 1] = j - i + 1
                else:
                    suffix[-j - 1] = min(j - i + 1, suffix[-j])
            elif j != 0:
                suffix[-j - 1] = suffix[-j]
        res = float('inf')
        for i in range(n):
            res = min(res, prefix[i] + suffix[i])
        return res if res != float('inf') else -1