"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meeting_times = []
        for interval in intervals:
            meeting_times.append([interval.start,1])
            meeting_times.append([interval.end,-1])
        meeting_times.sort()
        res = 0
        room_count = 0
        for meeting_time in meeting_times:
            room_count += meeting_time[1]
            res = max(res,room_count )
        return res
        