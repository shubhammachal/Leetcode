class Solution:
    def maximumLength(self, s: str) -> int:
        top3 = {chr(ord('a') + i):[0,0,0] for i in range(26)}
        n = len(s)
        i = 0

        while i < n:
            j = i
            while j < n and s[i] == s[j]:
                j += 1

            L = j - i
            self.push_top3(top3[s[i]], L)
            i = j

        ans = 0
        for l1, l2, l3 in top3.values():
            cand = max(l1 - 2, min(l1 - 1, l2), l3)
            if cand > ans:
                ans = cand
        return ans if ans > 0 else -1


    def push_top3(self, arr, x):
        if x > arr[0]:
            arr[0], arr[1], arr[2] = x, arr[0], arr[1]
        elif x > arr[1]:
            arr[1], arr[2] = x, arr[2]
        elif x > arr[2]:
            arr[2] = x

