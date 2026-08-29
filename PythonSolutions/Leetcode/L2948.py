class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups: list[list[list[int], int]] = []  # list of list curr idx and array
        curr_group = []
        group_mapper = {}
        for num in sorted(nums):
            if curr_group and num - curr_group[-1] > limit:
                groups.append([curr_group, 0])
                curr_group = []

            curr_group.append(num)
            group_mapper[num] = len(groups)
        groups.append([curr_group, 0])

        for i in range(len(nums)):
            group = groups[group_mapper[nums[i]]]
            nums[i] = group[0][group[1]]
            group[1] += 1

        return nums