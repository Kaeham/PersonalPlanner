from TimeSlotDay import TimeSlotDay
from datetime import date, timedelta

#testing imports
from PlannerList import PlannerList
from ListItem import ListItem

class TimeSlotWeek:
    def __init__(self, epoch_date) -> None:
        self.days = []
        epochWeekday = int(epoch_date.strftime("%w"))
        epoch_date -= timedelta(days=epochWeekday + 1)

        for _ in range(7):
            epoch_date += timedelta(days=1)
            newDay = TimeSlotDay(epoch_date)
            self.days.append(newDay)
        
    def get_days(self):
        for item in self.days:
            print(item)
    
    def __str__(self) -> str:
        res = ""
        for day in self.days:
            res += str(day)

        return res

today = date.today()
test = TimeSlotWeek(today)
test_ = test.days[0] # Single day in week

taskOneItemOne = ListItem("testOne", "Test for Item One")
taskOne = PlannerList("testOne", test_)
taskOne.add_item(taskOneItemOne)
test_.add_task(taskOne)
print(test)