import unittest
from classes.hotel_class import Hotel


class TestHotel(unittest.TestCase):
    def setUp(self):
        self.hotm = Hotel("Mariott", 4551325713, "79 16th Ave", 4)
        self.dummy = Hotel(None, None, None, 0)
        self.dummy.hotel_id = self.hotm.hotel_id
        self.hotm.output_file = "test" + str(TestHotel.counter) + ".json"
        self.dummy.output_file = "test" + str(TestHotel.counter) + ".json"
        TestHotel.counter += 1

    counter = 0
    def test_create_hotel_method_returns_correct_result(self):
        self.hotm.create_hotel()
        self.assertEqual({"hotel_name": "Mariott", "address": "79 16th Ave", "phone": 4551325713, "reserved_rooms": [], "available_rooms": [1, 2, 3, 4]}, self.dummy.display_hotel_info())

    def test_delete_hotel_method_returns_correct_result(self):
        self.hotm.create_hotel()
        self.hotm.delete_hotel()
        self.assertRaises(KeyError, self.dummy.display_hotel_info)

    def test_modify_info_method_returns_correct_result(self):
        self.hotm.create_hotel()
        self.hotm.modify_hotel_info("Marriot Fiesta", 555555555, "87 5th Ave")
        self.assertEqual({"hotel_name": "Marriot Fiesta", "address": "87 5th Ave", "phone": 555555555, "reserved_rooms": [], "available_rooms": [1, 2, 3, 4]}, self.dummy.display_hotel_info())
    
    def test_reserve_room_method_returns_correct_result(self):
        self.hotm.create_hotel()
        self.hotm.reserve_room()
        self.assertEqual({"hotel_name": "Mariott", "address": "79 16th Ave", "phone": 4551325713, "reserved_rooms": [1], "available_rooms": [2, 3, 4]}, self.dummy.display_hotel_info())

    def test_cancel_room_method_returns_correct_result(self):
        self.hotm.create_hotel()
        self.hotm.reserve_room()
        self.hotm.cancel_room(1)
        self.assertEqual({"hotel_name": "Mariott", "address": "79 16th Ave", "phone": 4551325713, "reserved_rooms": [], "available_rooms": [1, 2, 3, 4]}, self.dummy.display_hotel_info())



if __name__ == '__main__':
    unittest.main()