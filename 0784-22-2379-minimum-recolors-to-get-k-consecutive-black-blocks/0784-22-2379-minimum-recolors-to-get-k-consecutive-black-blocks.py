class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window_size = k
        n = len(blocks)
        w_count = 0
        min_op = float('inf')
        left = right = 0 
        #operations in first window
        for i in range(k):
            if blocks[i] == "W":
                w_count += 1
        min_op = min(w_count, min_op)

        for i in range(n-k):
            if blocks[i] == "W":
                w_count -= 1
            if blocks[k+i] == "W":
                w_count += 1
            min_op = min(w_count, min_op)
        return min_op

        