class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        def isOdd(num):
            return num % 2 != 0
        n = len(arr)
        for i in range(n-2):
            if isOdd(arr[i]) and isOdd(arr[i+1]) and isOdd(arr[i+2]):
                return True
        return False
        