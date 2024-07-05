from datetime import date
from PlannerList import PlannerList
from AuxMethods import Auxiliary as Aux


class TimeSlotDay:
    

    def __init__(self, date_time) -> None:
        self.date = date_time
        self.tasks = []

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

    def get_tasks(self):
        return self.tasks

    def __str__(self) -> str:
        res = ""
        res += self.date.strftime("%d %A") + "\n"
        for task in self.tasks:
            res+= str(task) + "\n"
        return res

today = date.today()
d3 = today.strftime("%A") # weekday in str form
d1 = today.strftime("%d") # day of month
d2 = today.strftime("%m") # month in int form


# print(today)