"""various approach to find the majority element
1. using count - time complexity O(n*n)
2. using hashmao - time complexity O(n), space complexity o(n)
3. divide and conquer - time complexity O(nlogn) space O(logn)
4. Boyer-Moore algortihm Linear time and O(1)
The basic idea behind this algorithm is to Cancel out each occurrence of the majority element with all other elements.
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        
        if nums.count(candidate) > len(nums) // 2:
            return candidate
        return None