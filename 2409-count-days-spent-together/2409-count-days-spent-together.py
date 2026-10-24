class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def date_to_day(date_str):
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days_in_month[:month - 1]) + day
        a_arrive = date_to_day(arriveAlice)
        a_leave = date_to_day(leaveAlice)
        b_arrive = date_to_day(arriveBob)
        b_leave = date_to_day(leaveBob)
        overlap_start = max(a_arrive, b_arrive)
        overlap_end = min(a_leave, b_leave)
        return max(0, overlap_end - overlap_start + 1)