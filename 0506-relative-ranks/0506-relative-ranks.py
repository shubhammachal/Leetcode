class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hm = {}
        for i, s in enumerate(score):
            hm[s] = i

        # Sort the scores in descending order
        sorted_scores = sorted(score, reverse=True)

     
        rank_list = [""] * len(score)

        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_list[hm[s]] = "Gold Medal"
            elif i == 1:
                rank_list[hm[s]] = "Silver Medal"
            elif i == 2:
                rank_list[hm[s]] = "Bronze Medal"
            else:
                # i is zero-based, so rank is i+1
                rank_list[hm[s]] = str(i + 1)

        return rank_list
