class Solution:
        def longestMountain(self, arr: List[int]) -> int:
            if len(arr) < 3:
                return 0
                
            max_len = 0
            for i in range(1, len(arr) - 1):  # Start from 1 to len-2
                if arr[i-1] < arr[i] > arr[i+1]:  # Found a peak
                    left = i - 1
                    right = i + 1
                    
                    while left > 0 and arr[left-1] < arr[left]:  # Expand left
                        left -= 1
                    while right < len(arr) - 1 and arr[right] > arr[right + 1]:  # Expand right
                        right += 1
                    
                    mountain_len = right - left + 1
                    max_len = max(max_len, mountain_len)
                    
            return max_len