class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # brute force for this one
        def find_array_min(arr1, dur1, arr2, dur2):
            min_arr = float('inf')            
            for x, y in zip(arr1, dur1):
                min_arr = min(min_arr, x + y)
            res = float('inf')
            for x, y in zip(arr2, dur2):
                res = min(res, max(x, min_arr) + y)
            return res
        res = find_array_min(landStartTime, landDuration, waterStartTime, waterDuration)
        res = min(res, find_array_min(waterStartTime, waterDuration, landStartTime, landDuration))
        return res