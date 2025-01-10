class Solution:
    def minSwaps(self, data: List[int]) -> int:
        #total number of ones in the array
        ones = sum(data)
        #edge case
        #if all ones or all zeros, or only one 1 no swap required
        if ones == len(data) or ones == 0 or ones == 1:
            return 0
        #initialize sliding window of fixed size
        window = ones
        zeros_in_window = sum(1 for i in range(window) if data[i] == 0)
        min_zeros = zeros_in_window
        #next window, add the next element of the array
        for i in range(window, len(data)):
            if data[i] == 0:
                zeros_in_window += 1
            #remove first element from the window
            if data[i - window] == 0:
                zeros_in_window -= 1

            min_zeros = min(min_zeros, zeros_in_window)
        return min_zeros




       