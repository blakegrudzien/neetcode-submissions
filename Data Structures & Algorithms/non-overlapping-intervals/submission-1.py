class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <2:
            return 0
        intervals = sorted(intervals, key = lambda x: (x[0],-x[1]))
        prev_end = intervals[0][1]
        i = 1
        removals = 0
        print(intervals)
        while i < len(intervals):
            if intervals[i][0]<prev_end:
                removals+=1
                prev_end = min(intervals[i][1],prev_end)
            else:
                prev_end = intervals[i][1]
            i+=1
        return removals
             


        