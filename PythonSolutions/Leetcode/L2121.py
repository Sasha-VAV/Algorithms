class Solution:
    def getDistances(self, nums: List[int]) -> List[int]:
        indices = defaultdict(list)
        ref_indices= {}
        for i, num in enumerate(nums):
            indices[num].append(i)
            ref_indices[i] = len(indices[num]) - 1

        l_prefixes = {}
        r_prefixes = {}

        for num, arr in indices.items():
            n = len(arr) + 1
            l_prefix = [0] * n
            r_prefix = [0] * n
            for i in range(n - 1):
                l_prefix[i + 1] = l_prefix[i] + arr[i]
                r_prefix[-i - 2] = r_prefix[-i - 1] + arr[-i - 1]
            l_prefixes[num] = l_prefix
            r_prefixes[num] = r_prefix
        
        res = []

        for i, num in enumerate(nums):
            idx = ref_indices[i]
            n = len(indices[num])
            x = indices[num][idx] * (2 * idx - n + 1)
            x -= l_prefixes[num][idx]
            x += r_prefixes[num][idx + 1]
            res.append(x)
        return res