class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days
        #intuition sort the intervals and merge (extension of merge intervals problem)
        # optimization is instead of storing merge intervals, can keep track of previous start and previous end
        meetings.sort()

        # Merge intervals while tracking occupied days
        prev_start, prev_end = meetings[0]
        occupied_days = 0

        for start, end in meetings[1:]:
            if start <= prev_end:  # Overlapping interval
                prev_end = max(prev_end, end)  # Merge
            else:
                occupied_days += prev_end - prev_start + 1  # Add previous segment length
                prev_start, prev_end = start, end  # Move to the next interval

        #Add the last merged interval's occupied days
        occupied_days += prev_end - prev_start + 1

        #Return the number of free days
        return days - occupied_days