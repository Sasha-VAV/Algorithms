class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        n = len(nums)
        def dfs(prefix, i):
            if i == n:
                if prefix not in nums:
                    return prefix
                else:
                    return None
            x = dfs(prefix+"0", i+1)
            if x: return x
            return dfs(prefix+"1", i+1)
        return dfs("", 0)