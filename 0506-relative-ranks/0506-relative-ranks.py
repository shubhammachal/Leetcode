import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        heap = []
        for idx, scores in enumerate(score):
            heapq.heappush(heap, (-scores,idx))

     
        rank_list = [""] * len(score)
        
        rank = 1
        while heap:
            orig_idx = heapq.heappop(heap)[1]
            if rank == 1:
                rank_list[orig_idx] = "Gold Medal"
            elif rank == 2:
                rank_list[orig_idx] = "Silver Medal"
            elif rank == 3:
                rank_list[orig_idx] = "Bronze Medal"
            else:
                rank_list[orig_idx] = str(rank )
            rank += 1

        return rank_list
