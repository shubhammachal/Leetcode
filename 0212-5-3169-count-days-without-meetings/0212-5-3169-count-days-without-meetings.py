class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        #intuition sort the intervals and merge
        #return days - len(sorted flatten array in the range(days))
        meetings.sort()
        merge = [meetings[0]]
        for start, end in meetings[1:]:
            last_end = merge[-1][1]
            if start <= last_end:
                merge[-1][1] = max(last_end, end)
            else:
                merge.append([start, end])
        occupied_days = sum(end - start + 1 for start, end in merge)
        return days - occupied_days
  
        