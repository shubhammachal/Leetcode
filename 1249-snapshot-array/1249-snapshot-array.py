class SnapshotArray:
    def __init__(self, length: int):
        self.length = length
        self.arr = [[[0, 0]] for _ in range(self.length)]  # Fixed
        self.curr_snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.arr[index][-1][1] == self.curr_snap_id:
            self.arr[index][-1][0] = val  # Fixed
        else:
            self.arr[index].append([val, self.curr_snap_id])

    def snap(self) -> int:
        self.curr_snap_id += 1
        return self.curr_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        left = 0
        history = self.arr[index]
        right = len(history) - 1
        result = history[0][0]
        while left <= right:
            mid = left + (right - left) // 2
            if history[mid][1] <= snap_id:  # Fixed
                result = history[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return result