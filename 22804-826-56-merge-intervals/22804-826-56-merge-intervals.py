class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort based on the first value
        intervals.sort(key = lambda x: x[0])
        # initialize res to first element of the itervals
        res = [intervals[0]]
        #iterate through end of the interval and compare end value of last interval in res with the start of the interval
        for start, end in intervals[1:]:
            last_end = res[-1][1]
            if start <= last_end:
                #max because we did sorted only for start value of the interval, for end val we need the maximum of end values of both the intervals
                res[-1][1] = max(last_end, end)
            else:
                res.append([start,end])
        return res
                





        