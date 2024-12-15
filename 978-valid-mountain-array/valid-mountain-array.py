class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        index_of_max = arr.index(max(arr))
        inc = False
        dec = False
        if len(arr) < 3:
            return False
        for i in range(index_of_max):
            if arr[i] < arr[i+1]:
                inc = True
            else:
                inc = False
                break
        
            
        for i in range(index_of_max, len(arr)-1):
            if arr[i] > arr[i+1]:
                dec = True
            else:
                dec = False
                break
        return inc and dec