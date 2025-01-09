class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        #brute force
        s = list(s)
        n = len(s)
        for direction, amount in shift:
            if direction == 0:
                amount %= n
                for _ in range(amount):
                    first = s.pop(0)
                    s.append(first)
            elif direction == 1:
                amount %= n
                for  _ in range(amount):
                    last = s.pop()
                    s.insert(0,last)
        return "".join(s)