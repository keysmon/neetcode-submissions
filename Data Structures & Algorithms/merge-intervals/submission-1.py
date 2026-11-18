class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key=lambda x:x[0])
        res = []
        pre_interval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] > pre_interval[1]: # not overlapping
                res.append(pre_interval)
                pre_interval = interval
            else:
                pre_interval = [pre_interval[0], max(pre_interval[1], interval[1])]
        res.append(pre_interval)
        return res
