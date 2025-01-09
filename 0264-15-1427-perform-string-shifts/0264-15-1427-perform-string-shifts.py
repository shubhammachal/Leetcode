class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)
        total_shift = 0

        # Calculate net shift
        for direction, amount in shift:
            if direction == 0:  # Left shift
                total_shift -= amount
            else:  # Right shift
                total_shift += amount

        # Reduce total shift within bounds of string length
        total_shift %= n

        # Perform the net shift
        s = s[-total_shift:] + s[:-total_shift]
        return s
