class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days
        #intuition sort the intervals and merge (extension of merge intervals problem)
        
        meetings.sort()
        merge = [meetings[0]]
        for start, end in meetings[1:]:
            last_end = merge[-1][1]
            if start <= last_end:
                merge[-1][1] = max(last_end, end)
            else:
                merge.append([start, end])
                
        #count total occupied days
        occupied_days = sum(end - start + 1 for start, end in merge)
        
        #return number of free days
        return days - occupied_days
  
        