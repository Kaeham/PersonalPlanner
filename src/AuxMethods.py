class Auxiliary:
    
    @staticmethod
    def add_to_list(list_to_add:list, item_to_add):
        list_to_add.append(item_to_add)

    @staticmethod 
    def delete_from_list(list_to_delete: list, index_to_delete):
        length = len(list_to_delete)
        tmpItem = list_to_delete[length - 1]                       # store item at end
        list_to_delete[length - 1] = list_to_delete[index_to_delete]     # move deleted item to the end
        list_to_delete[index_to_delete] = tmpItem                                 # add previous item at end to the location of the deleted item
        list_to_delete.pop()                                                # pop deleted item from list

    @staticmethod
    def find_index_of_item(list_to_search: list, item_to_find):
        i = 0
        for item in list_to_search:
            if item is item_to_find:
                Auxiliary.delete_from_list(list_to_search, i)
                return True
            else:
                i += 1