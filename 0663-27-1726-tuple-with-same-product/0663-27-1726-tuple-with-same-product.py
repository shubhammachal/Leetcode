class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        tuples = 0

        # Compute product frequencies
        for i in range(n):
            for j in range(i+1, n):
                prod = nums[i] * nums[j]
                freq[prod] = freq.get(prod, 0) + 1

        # Calculate the number of valid tuples
        for prod_freq in freq.values():
            pairs = (prod_freq * (prod_freq - 1)) // 2
            tuples += 8 * pairs

        return tuples