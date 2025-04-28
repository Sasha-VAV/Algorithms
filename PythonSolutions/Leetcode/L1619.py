class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        k = len(arr) // 20
        mid = sum(arr[k:-k])
        return mid / (len(arr) - k - k)        
