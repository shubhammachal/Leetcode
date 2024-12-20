def nextSmallest(nums):
    stack = []
    res = [-1] * len(nums)

    for i in range(len(nums)-1, -1,-1):
        while stack and nums[i] <= stack[-1]:
            stack.pop()

        if stack:
            res[i] = stack[-1]
        stack.append(nums[i])
    return res

print(nextSmallest(nums= [4,5,2,10,8]))
