class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        #intuition: find index of min from the start ans swap to bring min to front
        # then find index of max to from the right ans swap 
        #count total swap
        n = len(nums)
        #edge case
        if n == 1:
            return 0
        count = 0
        s_index = nums.index(min(nums))
        while nums[0] != nums[s_index]:
            nums[s_index], nums[s_index - 1] = nums[s_index - 1], nums[s_index]
            count += 1
            s_index -= 1
        #index of max from right
        m_index = n - 1
        for i in range(n - 1, -1, -1):
            if nums[i] > nums[m_index]:
                m_index = i
        #swap to bring max to the last

        while nums[n-1] != nums[m_index]:
            nums[m_index], nums[m_index + 1] = nums[m_index + 1], nums[m_index]
            count += 1
            m_index += 1
        return count
        