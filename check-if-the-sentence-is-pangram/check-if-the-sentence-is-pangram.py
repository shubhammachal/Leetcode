class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
        sen_set = set(sentence)
        return alphabet_set.issubset(sen_set)
            