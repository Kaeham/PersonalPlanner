from ListItem import ListItem

class List:
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
            self.listItems.append(item_to_add)
            self.listLength += 1

    def delete_item(self, item_to_delete):
        # test this (passed)
        if type(item_to_delete) is not ListItem:
            raise TypeError("Invalid Entry")
        i = 0
        for item in self.listItems:
            if item is item_to_delete:
                self.remove_entry_from_list(i)
                return True
            else:
                i += 1
        
        raise ValueError("Item is not in the list")
    
    def clear_items(self):
        self.listItems = []
        self.listLength = len(self.listItems)

    def remove_entry_from_list(self, index_one):
        # test this (passed)
        tmpItem = self.listItems[self.listLength - 1]                       # store item at end
        self.listItems[self.listLength - 1] = self.listItems[index_one]     # move deleted item to the end
        self.listItems[index_one] = tmpItem                                 # add previous item at end to the location of the deleted item
        self.listItems.pop()                                                # pop deleted item from list


    def change_time_slot():
        pass

    def change_list_order():
        pass 
