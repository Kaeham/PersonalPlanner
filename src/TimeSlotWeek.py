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

    def get_unq(self):
        for x in range(7):
            res = ""
            for x2 in range(7):
                res+= str(self.days[x].get_tasks() is self.days[x2].get_tasks()) + " "
            print(res)
    
    def __str__(self) -> str:
        res = ""
        print(self.days)
        for day in self.days:
            print(day)
            res += str(day)

        return ""
        return res

today = date.today()
test = TimeSlotWeek(today)
test_ = test.days[0] # Single day in week
print(test_)

taskOneItemOne = ListItem("testOne", "Test for Item One")
taskOne = PlannerList("testOne", test_)
test.get_unq()
taskOne.add_item(taskOneItemOne)
# test.get_days()
test_.add_task(taskOne)
# test.get_days()
# print(test)

