import unittest
from classes.reservation_class import Reservation
from classes.hotel_class import Hotel
from classes.costumer_class import Costumer


class TestReservation(unittest.TestCase):
    def setUp(self):
        self.hotm = Hotel("Mariott", 4551325713, "79 16th Ave", 4)
        self.dummy_hotm = Hotel(None, None, None, 0)
        self.dummy_hotm.hotel_id = self.hotm.hotel_id
        self.cost = Costumer("Hilario Rangel", 4551329423, "hil@gmail.com", 
                                1834572906421579)
        self.dummy_cost = Costumer(None, None, None, None)
        self.dummy_cost.costumer_id = self.cost.costumer_id
        self.res = Reservation(self.cost, self.hotm)
        self.dummy_res = Reservation(self.dummy_cost, self.dummy_hotm)
        self.dummy_res.reservation_id = self.res.reservation_id

        self.hotm.output_file = "testhotm" + str(TestReservation.counter) + ".json"
        self.cost.output_file = "testcost" + str(TestReservation.counter) + ".json"
        self.res.output_file = "testres" + str(TestReservation.counter) + ".json"
        self.dummy_hotm.output_file = "testhotm" + str(TestReservation.counter) + ".json"
        self.dummy_cost.output_file = "testcost" + str(TestReservation.counter) + ".json"
        self.dummy_res.output_file = "testres" + str(TestReservation.counter) + ".json"

        self.hotm.create_hotel()
        self.cost.create_costumer()
        TestReservation.counter += 1

    counter = 0

    def test_display_reservations_error_without_file(self):
        self.assertRaises(FileNotFoundError, self.dummy_res.display_reservation_info)

    def test_cancel_reservation_error_without_file(self):
        self.assertRaises(FileNotFoundError, self.dummy_res.cancel_reservation)

    def test_display_create_reservation_file_error(self):
        self.dummy_res.output_file = "corrupted.json"
        self.assertRaises(TypeError, self.dummy_res.create_reservation())
    
    def test_create_reservation_method_returns_correct_result(self):
        self.res.create_reservation()
        self.assertEqual({'costumer_name': self.cost.name,
                            'costumer_id': str(self.cost.costumer_id),
                            'hotel_name': self.hotm.name,
                            'hotel_id': str(self.hotm.hotel_id),
                            'reservatioin_id': str(self.res.reservation_id),
                            'room_number': self.res.room_number}, self.dummy_res.display_reservation_info())

    def test_delete_reservation_method_deletes_efectively(self):
        self.res.create_reservation()
        self.res.cancel_reservation()
        self.assertRaises(KeyError, self.dummy_res.display_reservation_info)





if __name__ == '__main__':
    unittest.main()