class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <2:
            return 0
        intervals = sorted(intervals, key = lambda x: (x[0],-x[1]))
        prev_end = intervals[0][1]
        removals = 0
        for start,end in intervals[1:]:
            if start<prev_end:
                removals+=1
                prev_end = min(end,prev_end)
            else:
                prev_end = end
        return removals
             


        