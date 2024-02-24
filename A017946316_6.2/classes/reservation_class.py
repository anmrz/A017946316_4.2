"""Class representing costumer"""
import json
import random
import string


class Reservation:
    """Represents a reservation"""
    def __init__(self, costumer, hotel):
        self.costumer_name = costumer.name
        self.costumer_id = costumer.costumer_id
        self.reservation_id = 'R' + ''.join(random.choices(string.digits, k=4))
        self.hotel = hotel
        self.room_number = -1
        self.output_file = "reservation.json"

    def create_reservation(self):
        """Find a room in hotel and creates a
        reservation and registers in file"""
        room_number = self.hotel.reserve_room()
        reservation_details = {'costumer_name': self.costumer_name,
                               'costumer_id': self.costumer_id,
                               'hotel_name': self.hotel.name,
                               'hotel_id': self.hotel.hotel_id,
                               'reservatioin_id': self.reservation_id,
                               'room_number': room_number}

        reservation_data = {self.reservation_id: reservation_details}
        try:
            with open(self.output_file, "r") as outfile:
                current_data = json.load(outfile)
                current_data.update(reservation_data)
        except FileNotFoundError:
            current_data = reservation_data
        reservation_json = json.dumps(current_data)
        with open(self.output_file, "w") as outfile:
            outfile.write(reservation_json)
        self.room_number = room_number
        return reservation_details

    def cancel_reservation(self):
        """Cancels a reservation"""
        self.hotel.cancel_room(self.room_number)
        try:
            with open(self.output_file, "r") as outfile:
                current_data = json.load(outfile)
                del current_data[self.reservation_id]
                print(current_data)
                with open(self.output_file, "w") as outfile:
                    reservation_json = json.dumps(current_data)
                    outfile.write(reservation_json)
        except FileNotFoundError:
            print("File couldn't be found")
            raise
        except KeyError:
            print("Reservation does not exist in list")
            raise
        except TypeError:
            print("dict' object is not callable")
            raise

    def display_reservation_info(self):
        """Shows reservation info from file"""
        try:
            with open(self.output_file, "r") as outfile:
                current_data = json.load(outfile)
                return current_data[self.reservation_id]
        except FileNotFoundError:
            print("File not found")
            raise
        except KeyError:
            print("Costumer does not exist in file")
            raise
            