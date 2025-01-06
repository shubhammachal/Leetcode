class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        s = list(s)
        #we will use a difference array and prefix sum
        diff_arr = [0] * (n + 1)
        #for diff array, we need to update end + 1
        for start, end, direction in shifts:
            shift_dir = 1 if direction == 1 else -1
            diff_arr[start] += shift_dir
            if end + 1 < n:
                diff_arr[end+1] -= shift_dir
        #cumulative sum which will be the net shift for each element
        net_shift = 0
        for i in range(n):
            net_shift += diff_arr[i]
            s[i] = chr((ord(s[i]) - ord('a') + net_shift ) % 26 + ord('a'))
        return "".join(s)
