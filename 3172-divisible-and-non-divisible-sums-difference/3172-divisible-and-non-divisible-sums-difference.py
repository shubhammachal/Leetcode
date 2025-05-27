class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        #total sum
        total_sum = n*(n+1) // 2
        #edge cases
        if m > n:
            return total_sum
        if n == 1:
            return -1 if m == 1 else 1
        
        # multiples of m in the range[1,n] let's say k
        k = n // m
        #sum of numbers divisible by m
        num2 = m * (k*(k+1)//2)
        #sum of numbers not divisible by m
        num1 = total_sum - num2
        return num1 - num2


