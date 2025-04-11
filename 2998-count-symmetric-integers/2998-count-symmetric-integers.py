class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        
        for num in range(low, high+1):
            num_str = str(num)
            length = len(str(num_str))
            if length % 2 == 0:
                digits = [int(digit) for digit in num_str]
                first_half_sum = sum(digits[:length//2])
                second_half_sum = sum(digits[length//2:])
                if first_half_sum == second_half_sum:
                    count += 1
        return count