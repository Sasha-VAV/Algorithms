class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        curr_diff = float('inf')
        pairs = []
        for i in range(0, len(arr) - 1):
            if arr[i+1] - arr[i] < curr_diff:
                curr_diff = arr[i+1] - arr[i]
                pairs = []
            if arr[i+1] - arr[i] == curr_diff:
                pairs.append([arr[i], arr[i+1]])
        return pairs