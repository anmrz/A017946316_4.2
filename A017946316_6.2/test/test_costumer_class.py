import unittest
from classes.costumer_class import Costumer
import os

class TestCostumer(unittest.TestCase):
    def setUp(self):
        self.cost = Costumer("Hilario Rangel", 4551329423, "hil@gmail.com", 
                                1834572906421579)
        self.dummy = Costumer(None, None, None, None)
        self.dummy.costumer_id = self.cost.costumer_id
        self.cost.output_file = "testcost" + str(TestCostumer.counter) + ".json"
        self.dummy.output_file = "testcost" + str(TestCostumer.counter) + ".json"
        TestCostumer.counter += 1

    counter = 0

    def test_display_customer_error_raise_withouth_file(self):
        self.assertRaises(FileNotFoundError, self.dummy.display_costumer_info)

    # def test_modify_customer_error_raise_withouth_file(self):
    #     self.assertRaises(FileNotFoundError, self.dummy.modify_costumer_info, (00000000, "xx@gmail.com", 
    #                             180000421005700))
    
    def test_error_raise_deleting_withouth_file(self):
        self.assertRaises(FileNotFoundError, self.dummy.delete_costumer)

    def test_create_costumer_method_returns_correct_result(self):
        self.cost.create_costumer()
        self.assertEqual({"name": "Hilario Rangel", 
                            "phone": 4551329423,
                            "card": 1834572906421579,
                            "email": "hil@gmail.com"}, self.dummy.display_costumer_info())

    def test_delete_costumer_method_returns_correct_result(self):
        self.cost.create_costumer()
        self.cost.delete_costumer()
        self.assertRaises(KeyError, self.dummy.display_costumer_info)

    

    def test_modify_info_method_returns_correct_result(self):
        self.cost.create_costumer()
        self.cost.modify_costumer_info(8551329489, "hila@gmail.com", 784572906400000)
        self.assertEqual({"name": "Hilario Rangel",
                            "phone": 8551329489,
                            "card": 784572906400000,
                            "email": "hila@gmail.com"}, self.dummy.display_costumer_info())



if __name__ == '__main__':
    unittest.main()