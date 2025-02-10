class Solution:
    def clearDigits(self, s: str) -> str:
        res = list(s)
        i = 0
        while i < len(res):
            if res[i].isdigit():
                if i > 0 and not res[i-1].isdigit():
                    del res[i]
                    del res[i-1]
                    i = max(0, i-1)
                else:
                    i += 1
            else:
                i += 1
        return "".join(res)
        

        