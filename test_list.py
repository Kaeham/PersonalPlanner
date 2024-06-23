import unittest

from PlannerList import List
from ListItem import ListItem

class TestList(unittest.TestCase):
    testList = List("test", "any")


    def test_add(self):
        """
        test addition of items to the list
        """
        entry = ListItem("test", "test")
        self.testList.add_item(entry)
        self.assertTrue(entry in self.testList.get_items())
        self.assertEqual(self.testList.listLength, 1)


    def test_add_invalid_entry(self):
        """
        test addition of invalid items
        """
        entry = 1
        self.assertRaises(TypeError, lambda: self.testList.add_item(entry))
    
    def test_delete(self):
        """
        test deletion of item from the list
        """
        entries = [
            ListItem("test", "test"), ListItem("test1", "test1"),
            ListItem("test2", "test2"), ListItem("test3", "test3")
            ]

        for entry in entries:
            print(entry)
            self.testList.add_item(entry)
        
        self.assertTrue(entries[0] in self.testList.get_items())
        self.testList.delete_item(entries[0])
        self.assertFalse(entries[0] in self.testList.get_items())

    def test_order_of_items(self):
        """
        test that order of items after deletion remains the same
        """
        pass

if __name__ == "__main__":
    unittest.main()
        
        
