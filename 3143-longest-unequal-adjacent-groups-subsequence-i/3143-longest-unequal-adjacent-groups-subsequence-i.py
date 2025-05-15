class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # Start with 0
        subseq0 = []
        expected = 0
        
        for i in range(len(groups)):
            if groups[i] == expected:
                subseq0.append(words[i])
                expected = 1 - expected  # Flip between 0 and 1
                
        # Reset and start with 1
        subseq1 = []
        expected = 1
        
        for i in range(len(groups)):
            if groups[i] == expected:
                subseq1.append(words[i])
                expected = 1 - expected  # Flip between 0 and 1
                
        # Return the longer subsequence
        if len(subseq0) >= len(subseq1):
            return subseq0
        else:
            return subseq1