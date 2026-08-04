class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # O(3N) but better for memory
        min_number = nums[0]
        max_number = nums[0]

        for num in nums:
            min_number = min(min_number, num)
            max_number = max(max_number, num)
        
        seen = [0] * (max_number - min_number + 1)
        for num in nums:
            seen[num - min_number] = 1
        
        return [i for i in range(min_number + 1, max_number) if not seen[i - min_number]]