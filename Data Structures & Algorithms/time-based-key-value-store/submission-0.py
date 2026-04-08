class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]
        res = ""
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
        
