class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Rearranges numbers into the lexicographically next greater permutation.
        Modifies nums in-place.
        """
        n = len(nums)
        pivot_found = False
        
        # find the pivot which is first element that is smaller than the 
        #element from it's right while iterating from the end
        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot_idx = i-1
                pivot_found = True
                break
        
        if not pivot_found:
            # if the array is in ascending order(no pivot element found), reverse it to the smallest permutation
            nums.reverse()
            return
        
        # find the successor, first element from the right which is greater than the pivot element
        for i in range(n-1, pivot_idx, -1):
            if nums[i] > nums[pivot_idx]:
                succ_idx = i
                break
        
        # Sswap pivot and successor
        nums[pivot_idx], nums[succ_idx] = nums[succ_idx], nums[pivot_idx]
        
        # reverse the suffix(subarray after pivot till end)
        left, right = pivot_idx + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
