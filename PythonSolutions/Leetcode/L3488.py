from collections import defaultdict


class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)
        ref = defaultdict(list)
        for i, num in enumerate(nums):
            ref[num].append(i)
        shift = {}
        for arr in ref.values():
            if len(arr) == 1:
                shift[arr[0]] = -1
                continue
            for i, x in enumerate(arr):
                if i == 0:
                    shift[x] = n - arr[-1] + x
                else:
                    shift[x] = x - arr[i - 1]

                if i == len(arr) - 1:
                    shift[x] = min(shift[x], n + arr[0] - x)
                else:
                    shift[x] = min(shift[x], arr[i + 1] - x)


        res = []
        for i in queries:
            res.append(shift[i])
        return res


if __name__ == "__main__":
    nums = [1,3,1,4,1,3,2]
    queries = [0,3,5]
    print(Solution().solveQueries(nums, queries))