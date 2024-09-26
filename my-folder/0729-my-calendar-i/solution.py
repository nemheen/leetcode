import bisect

class MyCalendar:

    def __init__(self):
        self.cal = []
        

    def book(self, st: int, end: int) -> bool:
        
        i = bisect.bisect_left(self.cal, (st, end))
        # is is found comparing tuples based on st, if first els equal, compare the sec el

        if i > 0 and self.cal[i-1][1] > st:
            return False
        if i < len(self.cal) and self.cal[i][0] < end:
            return False

        self.cal.insert(i, (st, end))

        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
