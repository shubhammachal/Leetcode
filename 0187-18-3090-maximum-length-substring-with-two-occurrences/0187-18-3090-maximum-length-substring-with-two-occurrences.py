class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        def is_valid(substring: str) -> bool:
        # Count frequency of characters in the substring
            char_count = {}
            for char in substring:
                char_count[char] = char_count.get(char, 0) + 1
                if char_count[char] > 2:
                    return False  # If any character appears more than twice, return False
            return True

        max_length = 0
        n = len(s)

        # Generate all substrings using nested loops
        for i in range(n):
            for j in range(i+1, n+1):
                substring = s[i:j]
                if is_valid(substring):
                    max_length = max(max_length, j - i)

        return max_length