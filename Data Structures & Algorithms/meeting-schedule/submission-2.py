"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        s = sorted(intervals, key = lambda s: s.start)
        time = 0
        for i in s:
            if time > i.start:
                return False
            time = i.end 
        return True 
            


