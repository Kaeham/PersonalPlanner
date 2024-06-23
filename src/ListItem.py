class ListItem:
    status = False


    def __init__(self, name, desc) -> None:
        self.name = name
        self.desc = desc

    def edit_item(self, name=None, desc=None):
        # test this
        if name != None:
            self.name = name
        if desc != None:
            self.desc = desc

    def __str__(self) -> str:
        res = ""
        res += self.name + " " + self.desc
        return res

    # def edit_name():
    #     pass

    # def edit_desc():
    #     pass