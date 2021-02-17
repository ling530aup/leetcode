class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals = sorted(intervals, key=lambda x:x[0])
        rt = [intervals[0]]
        for i in range(1,len(intervals)):
            if rt[-1][1] < intervals[i][0]:
                rt.append(intervals[i])
            else:
                if intervals[i][1] > rt[-1][1]:
                    rt[-1][1] = intervals[i][1]
        return rt
      
