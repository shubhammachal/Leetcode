def nextGreater(nums):
    res = [-1] * len(nums)
    stack = []

    for i in range(len(nums) -1 , - 1, -1):
        #maintain decreasing order in the stack
        # if current is greater than the top, then the decreasing order in stack is violated
        # so pop the element and then push the current
        while stack and nums[i] >= stack[-1]:
            stack.pop()
        
        if stack:
            res[i] = stack[-1]
            
        stack.append(nums[i])
    return res
print(nextGreater(nums= [4,5,2,10,8]))