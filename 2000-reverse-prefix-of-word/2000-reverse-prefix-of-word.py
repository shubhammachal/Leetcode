class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left = 0
        word = list(word)
        
        for right in range(len(word)):
            if word[right] == ch:
                while left < right:
                    word[left], word[right] = word[right], word[left]
                    left += 1
                    right -= 1
                    
                return "".join(word)
        return "".join(word)