class TimeMap:

    def __init__(self):
        self.kt = dict()
        self.tv = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kt[key] = self.kt.get(key, list()) + [timestamp]
        self.tv[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        arr = self.kt.get(key, list())
        if len(arr) == 0:
            return ""
        left, right = 0, len(arr) - 1
        if arr[left] > timestamp:
            return ""
        while left < right:
            mid = (left + right + 1) // 2
            if arr[mid] < timestamp:
                left = mid
            elif arr[mid] > timestamp:
                right = mid - 1
            else:
                return self.tv[arr[mid]]
        return self.tv[arr[left]]

