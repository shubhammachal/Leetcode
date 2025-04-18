class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        n = len(arr)
    
        i = n - 1
        j = n + zeros - 1
    
        while i < j:
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
            
                if j < n:
                    arr[j] = 0
            i -= 1
            j -= 1

            
        
            