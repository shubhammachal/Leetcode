class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        altitudes = [0] * (n+1)
        altitudes[0] = 0
        max_alt = float('-inf')
        for i in range(1, n+1):
            altitudes[i] = altitudes[i-1] + gain[i-1]
        for i in range(n+1):
            if altitudes[i] > max_alt:
                max_alt = altitudes[i]
        return max_alt