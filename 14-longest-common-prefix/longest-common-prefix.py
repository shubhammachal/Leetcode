class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        for s in strs[1:]:
            # Reduce the prefix by comparing it with each string
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                # If the prefix becomes empty, return ""
                if not prefix:
                    return ""
        
        return prefix


