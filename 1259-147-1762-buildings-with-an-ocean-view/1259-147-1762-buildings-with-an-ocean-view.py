class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        n = len(heights)
        max_so_far = heights[-1]
        #rightmost index will always have ocean view
        for i in range(n-1, -1, -1):
            if heights[i] > max_so_far:
                max_so_far = heights[i]
                res.append(i)
        res.append(n-1)
        return sorted(res)
                

            