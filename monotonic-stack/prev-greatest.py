def prevGreatest(nums):
    stack = []
    res = [-1] * len(nums)
    for i in range(len(nums)):
        while stack and nums[i] >= stack[-1]: #prev should be greater so maintain monotonically decreasing order
            stack.pop()

        if stack:
            res[i] = stack[-1]
        stack.append(nums[i])

    return res
print(prevGreatest(nums = [4,5,2,10,8]))