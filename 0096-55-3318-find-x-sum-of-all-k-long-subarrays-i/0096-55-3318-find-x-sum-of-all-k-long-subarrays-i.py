import heapq
from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        #1. Define a function to calculate `xSum` using frequency counts and a heap.
        def xSum(freq, x):
            heap = []
            for key, value in freq.items():
                heapq.heappush(heap, (value, key))
                if len(heap) > x:
                    heapq.heappop(heap)
            return sum(num[0] * num[1] for num in heap)


        #2. Initialize sliding window of size `k`
            #Compute frequency of first `k` elements.
            #Calculate sum of top `x` frequent elements.
        freq = Counter(nums[:k])
        n = len(nums)
        left = 0
        ans = [0] * (n - k + 1)
        ans[0] = xSum(freq, x)

        #3. Slide the window:
            #Remove the element going out of the window.
            #Add the new element coming in.
            #Update the frequency dictionary and heap accordingly.
        for right in range(k, n):
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1
            freq[nums[right]] += 1

            ans[left] = xSum(freq, x)
        return ans

