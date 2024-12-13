'''Brute Force: check sum of each element with every other element 
time complexity: O(n^2), space complexity: O(1)
Using hashmap, time complexity: O(n), space complexity: O(n)'''

def two_sum(nums, target):
    seen = {}  # Using a dictionary for O(1) lookup
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return (seen[diff], i)  # Return indices in the correct order
        seen[num] = i  # Store the current number and its index
    return None  # If no solution is found

nums = [3,4,5,6]
target = 7
print(two_sum(nums,target))

