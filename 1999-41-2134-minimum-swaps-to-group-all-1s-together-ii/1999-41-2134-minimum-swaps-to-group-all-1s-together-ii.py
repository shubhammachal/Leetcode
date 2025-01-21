class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        #number of ones is window size
        total_ones = sum(nums)
        n = len(nums)
        if total_ones == 0 or total_ones == 1 or total_ones == n:
            return 0
        window_size = total_ones
        zeros_in_window = sum(1 for i in range(window_size) if nums[i] == 0)
        min_zeros = zeros_in_window

        #update window with wrap around as array is circular
        #option 1. extend array as nums + nums
        #option 2. wrap around with modulo

        for i in range(n):
            if nums[i % n] == 0:
                zeros_in_window -= 1
            if nums[(i + window_size) % n] == 0:
                zeros_in_window += 1
            min_zeros = min(min_zeros, zeros_in_window)
        return min_zeros