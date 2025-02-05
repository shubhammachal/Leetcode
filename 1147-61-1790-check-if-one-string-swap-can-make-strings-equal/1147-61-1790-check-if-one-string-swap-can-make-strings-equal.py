class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        first_mis_idx = second_mis_idx = 0
        mismatched_count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatched_count += 1
                
                if mismatched_count > 2:
                    return False

                elif mismatched_count == 1:
                    first_mis_idx = i
                elif mismatched_count == 2:
                    second_mis_idx = i
                    
        return (s1[first_mis_idx] == s2[second_mis_idx] and s1[second_mis_idx] == s2[first_mis_idx])
                