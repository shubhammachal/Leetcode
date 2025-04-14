class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        target_dist = abs(0-target[0])  + abs(0-target[1]) 
        for start, end in ghosts:
            g_dist = abs(start - target[0])  + abs(end - target[1]) 
            if g_dist <= target_dist:
                return False
        return True