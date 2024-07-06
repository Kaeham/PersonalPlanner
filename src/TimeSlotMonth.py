from TimeSlotDay import TimeSlotDay
from TimeSlotWeek import TimeSlotWeek
from datetime import date, timedelta

class TimeSlotMonth:
    def __init__(self, epoch_date) -> None:
        self.weeks = []
        epochDay = int(epoch_date.strftime("%d"))
        # print(epochDay)
        epoch_date -= timedelta(days=epochDay)
        print(epoch_date)



d = date.today()
d = d.strftime("%d")
# print(d)
a = TimeSlotMonth(date.today())