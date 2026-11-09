class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        res = []
        for start, end in intervals:
            if start > curr_end:
                res.append([curr_start,curr_end])
                curr_start = start
                curr_end = end
            else:
                curr_end = max(curr_end, end)
        res.append([curr_start, curr_end])
        return res
             

        