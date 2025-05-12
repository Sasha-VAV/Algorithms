from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        nums = [0] * 10
        for digit in digits:
            if nums[digit] < 3: nums[digit] += 1
        def make_nums(s, counts):
            if len(s) == 3:
                if int(s) % 2 == 0 and int(s) // 100 > 0:
                    return {int(s)}
                return set()
            ans = set()
            for i, count in enumerate(counts):
                if count == 0:
                    continue
                new_counts = counts.copy()
                new_counts[i] -= 1
                ans = ans.union(make_nums(s+str(i), new_counts))
            return ans
        return sorted(list(make_nums("", nums)))


# My 200th solution on LeetCode
if __name__ == '__main__':
    print(Solution().findEvenNumbers([2, 1, 3, 0]))