class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hash_set = set()
        for char in s:
            if char in hash_set:
                return char
            hash_set.add(char)