class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False
    
'''Brute Force: compare each element with every othe element. time complexity: O(n^2), space complexity: O(1)
sort and compare adjacent elements, time complexity: O(nlogn), space complexity: O(1)
creating hashset: time complexity = O(n), space complexity: O(n)
we can also use return set(nums) != nums time complexity = O(n), 
space coplexity is also O(n) -  worst case set will contain all the elements'''