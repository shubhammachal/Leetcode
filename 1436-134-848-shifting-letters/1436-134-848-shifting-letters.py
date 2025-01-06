class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shifts = 0
        s = list(s)
        for i in range(len(s)-1, -1, -1):
            total_shifts += shifts[i]
            s[i] = chr((ord(s[i]) - ord('a') + total_shifts ) % 26 + ord('a'))
        return "".join(s)
