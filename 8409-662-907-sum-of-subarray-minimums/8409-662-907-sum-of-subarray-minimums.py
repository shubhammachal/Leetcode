class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        sum_of_minimus = 0
        for i in range(len(arr)+1):
        #i == len(arr) all elements are processed and stack is not empty
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                #if stack is empty left is -1
                left = -1 if not stack else stack[-1]
                right = i

                no_subarrays_where_mid_is_min = (mid-left) * (right-mid)
                sum_of_minimus += no_subarrays_where_mid_is_min * arr[mid]

            stack.append(i)
        return sum_of_minimus % (10**9 + 7)