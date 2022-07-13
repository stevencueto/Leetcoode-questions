class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda i : i[0])
        
        for i in range(1, len(intervals)):
            m1 = intervals[i - 1]
            m2 = intervals[i]
            
            if m1[1] > m2[0]:
                return False
        return True