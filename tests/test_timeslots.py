import unittest

from src.TimeSlotDay import TimeSlotDay

class TestList(unittest.TestCase):
    testDay = TimeSlotDay()


    def test_add(self):
        """
        test addition of items to the list
        """
        pass


    def test_add_invalid_entry(self):
        """
        test addition of invalid items
        """
        pass
    
    def test_delete(self):
        """
        test deletion of item from the list
        """
        pass

    def test_order_of_items(self):
        """
        test that order of items after deletion remains the same
        """
        pass

if __name__ == "__main__":
    unittest.main()
        
        
