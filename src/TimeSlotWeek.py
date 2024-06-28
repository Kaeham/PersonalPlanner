from TimeSlotDay import TimeSlotDay
from datetime import date, timedelta

class TimeSlotWeek:
    def __init__(self, epoch_date) -> None:
        self.days = []
        epochWeekday = int(epoch_date.strftime("%w"))
        epoch_date -= timedelta(days=epochWeekday)

        for x in range(7):
            epoch_date += timedelta(days=x)
            self.days.append(TimeSlotDay(epoch_date))

today = date.today()
epochWeekday = int(today.strftime("%w"))
today -= timedelta(days=epochWeekday)
print(today)

