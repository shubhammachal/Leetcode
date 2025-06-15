class Solution:
    def maxDiff(self, num: int) -> int:
        max_num, min_num = str(num), str(num)

        for digit in max_num:
            if digit != "9":
                max_num = max_num.replace(digit, "9")
                break
        
        for i, digit in enumerate(min_num):
            if i == 0:
                if digit != "1":
                    min_num = min_num.replace(digit, '1')
                    break
            else:
                if digit != "0" and digit != min_num[0]:
                    min_num = min_num.replace(digit, "0")
                    break
        return int(max_num) - int(min_num)
            