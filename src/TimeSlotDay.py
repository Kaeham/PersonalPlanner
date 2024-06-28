from datetime import date
from PlannerList import PlannerList
from AuxMethods import Auxiliary as Aux


class TimeSlotDay:
    tasks = []

    def __init__(self, date_time) -> None:
        self.date = date_time

    def add_task(self, task_to_add) -> None:
        if type(task_to_add) is not PlannerList:
            raise TypeError("Item is not a task")
        else:
            Aux.add_to_list(self.tasks, task_to_add)

    def delete_task(self, task_to_delete) -> None:
        if type(task_to_delete) is not PlannerList:
            raise TypeError("Ivalid Item")

    def change_list_order(self, task_one, task_two) -> None:
        pass

today = date.today()
d3 = today.strftime("%A")
d1 = today.strftime("%d")
d2 = today.strftime("%m")
print(d3, d1, d2)
print(today)