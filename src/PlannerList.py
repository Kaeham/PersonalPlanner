from ListItem import ListItem
from AuxMethods import Auxiliary as Aux

class PlannerList:
    listItems = []
    listLength = len(listItems)

    def __init__(self, name, time_slot) -> None:
        self.name = name
        self.timeSlot = time_slot

    def get_items(self):
        return self.listItems
    
    def add_item(self, item_to_add):
        # test this (passed)
        if type(item_to_add) is not ListItem:
            raise TypeError("Invalid Entry")
        else:
            Aux.add_to_list(self.listItems, item_to_add)
            self.listLength += 1

    def delete_item(self, item_to_delete):
        # test this (passed)
        if type(item_to_delete) is not ListItem:
            raise TypeError("Invalid Entry")
        index = Aux.find_index_of_item(self.listItems, item_to_delete)
        if not index:
            raise ValueError("Item is not in the list")
        else:
            Aux.delete_from_list(self.listItems, index) 
            
    
    def clear_items(self):
        self.listItems = []
        self.listLength = len(self.listItems)


    def change_time_slot():
        pass

    def change_list_order():
        pass 
