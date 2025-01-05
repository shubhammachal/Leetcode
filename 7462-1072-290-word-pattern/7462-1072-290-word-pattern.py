class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        # if lenghts are not equal, return False
        if len(pattern) != len(words):
            return False

        #two dict for char to word mapping and word to char mapping
        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            #char to word mapping
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
            
            #word to char mapping

            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        #return true after all the checks
        return True