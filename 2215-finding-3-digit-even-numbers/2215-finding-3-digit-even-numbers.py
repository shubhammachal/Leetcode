from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        res = set()
        for first in range(1,10):
            if first not in freq or freq[first] <= 0:
                continue
            freq[first] -= 1

            for second in range(10):
                if second not in freq or freq[second] <= 0:
                    continue
                freq[second] -= 1

                for third in range(0,10,2):
                    if third not in freq or freq[third] <= 0:
                        continue
                    num = first * 100 + second * 10 + third
                    res.add(num)

                freq[second] += 1
            freq[first] += 1
        return sorted(list(res))
