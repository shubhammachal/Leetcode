class Solution:
    def maximumLength(self, s: str) -> int:
        count = {}
        for start in range(len(s)):
            for end in range(start, len(s)):
                substring = s[start:end+1]
                if self.is_special(substring):
                    count[substring] = count.get(substring, 0) + 1

        max_len = -1
        for substring, freq in count.items():
            if freq >= 3:
                max_len = max(max_len, len(substring))
        return max_len

    def is_special(self, s: str) -> bool:
        return len(set(s)) == 1 if s else False
