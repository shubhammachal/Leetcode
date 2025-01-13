class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        #increment i if both are same otherwise increment j
        #if we have successfully iterated s, means s is the subseq of t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)