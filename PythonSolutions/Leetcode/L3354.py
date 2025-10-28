from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        res = 0
        multipliers = {}
        new_nums = []
        for num in nums:
            if num > 0:
                new_nums.append(num)
                continue
            if not new_nums or new_nums[-1] != 0:
                multipliers[len(new_nums)] = 1
                new_nums.append(0)
            else:
                multipliers[len(new_nums) - 1] += 1
        nums = new_nums
        def search(arr, i, right_direction):
            if not 0 <= i < len(arr):
                return sum(arr) == 0
            if arr[i] == 0:
                return search(arr, i + (1 if right_direction else -1), right_direction)
            arr[i] -= 1
            right_direction = not right_direction
            return search(arr, i + (1 if right_direction else -1), right_direction)

        for i, num in enumerate(nums):
            if num != 0: continue
            res += (search(nums.copy(), i, True) + search(nums.copy(), i, False)) * multipliers[i]
        return res


if __name__ == '__main__':
    test_arr = [1,0,2,0,3]
    print(Solution().countValidSelections(test_arr))