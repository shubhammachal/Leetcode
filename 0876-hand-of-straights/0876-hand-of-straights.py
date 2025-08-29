from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)

        n = len(hand)
        if n % groupSize != 0:
            return False
        
        for num in sorted(freq.keys()):
            while freq[num] > 0:
                for i in range(groupSize):
                    if freq[num+i] <= 0:
                        return False
                    freq[num + i] -= 1
        return True