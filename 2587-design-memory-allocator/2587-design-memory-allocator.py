class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.memory = [0] * n
        

    def allocate(self, size: int, mID: int) -> int:
        if size <= 0 or size > self.n:
            return -1
        consecutive_count = 0
        for i in range(self.n):
            if self.memory[i] == 0:
                consecutive_count += 1
                if consecutive_count == size:
                    start_index = i - size + 1
                    for j in range(start_index, i + 1):
                        self.memory[j] = mID
                    return start_index
            else:
                consecutive_count = 0
        return -1
        

    def freeMemory(self, mID: int) -> int:
        count = 0
        for i in range(self.n):
            if self.memory[i] == mID:
                count += 1
                self.memory[i] = 0
        return count



# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)