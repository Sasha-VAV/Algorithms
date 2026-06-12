class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low_q = []
        middle = 0
        high_q = []
        for num in nums:
            if num < pivot:
                low_q.append(num)
            elif num > pivot:
                high_q.append(num)
            else:
                middle += 1
        return low_q + [pivot] * middle + high_q