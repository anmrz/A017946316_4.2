"""Hotel class"""
import json
import random
import string

class Hotel:
    """A class represents a hotel"""
    def __init__(self, name, phone, address, number_rooms):
        self.name = name
        self.phone = phone
        self.address = address
        self.available_rooms = list(range(1, number_rooms + 1))
        self.reserved_rooms = []
        self.hotel_id = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=4))
        self.output_file = 'hotel.json'
    def create_hotel(self):
        """Creates a hotel and registers in file"""
        hotel_data = {self.hotel_id: {
                                      'hotel_name': self.name,
                                      'address': self.address,
                                      'phone': self.phone,
                                      'reserved_rooms': self.reserved_rooms,
                                      'available_rooms': self.available_rooms}}
        try:
            with open(self.output_file, "r") as outfile:
                current_data = json.load(outfile)
                current_data.update(hotel_data)
        except FileNotFoundError:
            current_data = hotel_data
        except json.decoder.JSONDecodeError:
            current_data = hotel_data

        hotel_json = json.dumps(current_data)
        with open(self.output_file, "w+") as outfile:
            outfile.write(hotel_json)
        return hotel_json

    def delete_hotel(self):
        """Deletes a hotel instance in a json file"""
        with open(self.output_file) as outfile:
            current_data = json.load(outfile)
        try:
            del current_data[self.hotel_id]
            hotel_json = json.dumps(current_data)
            with open(self.output_file, "w") as outfile:
                outfile.write(hotel_json)
        except KeyError:
            return

    def display_hotel_info(self):
        """Shows hotel info from file"""
        try:
            with open(self.output_file, "r") as outfile:
                current_data = json.load(outfile)
                return current_data[self.hotel_id]
        except FileNotFoundError:
            print("File doesn't exist")
        except KeyError:
            print("Hotel info couldn't be found on file")
            raise

    def modify_hotel_info(self, name, phone, address):
        """Modifies hotel info in a json file"""
        self.name = name
        self.phone = phone
        self.address = address
        with open(self.output_file) as outfile:
            current_data = json.load(outfile)
        try:
            current_data[self.hotel_id]['hotel_name'] = self.name
            current_data[self.hotel_id]['phone'] = self.phone
            current_data[self.hotel_id]['address'] = self.address
            hotel_json = json.dumps(current_data)
            with open(self.output_file, "w") as outfile:
                outfile.write(hotel_json)
        except KeyError:
            raise

    def reserve_room(self):
        """Find an available room and reserves it"""
        room_number = -1
        try:
            with open(self.output_file) as outfile:
                current_data = json.load(outfile)
                if current_data[self.hotel_id]['available_rooms']:
                    room_number = current_data[self.hotel_id][
                        'available_rooms'].pop(0)
                    current_data[self.hotel_id][
                        'reserved_rooms'].append(room_number)
                    with open(self.output_file, "w") as outfile:
                        hotel_json = json.dumps(current_data)
                        outfile.write(hotel_json)
                else:
                    print(f"There is not an available room at {self.name}")
        except KeyError:
            print("Hotel info couldn't be found on file")
        return room_number

    def cancel_room(self, room_number):
        """Cancels a reserved room"""
        with open(self.output_file) as outfile:
            current_data = json.load(outfile)
            reserved_rooms = set(current_data[self.hotel_id]['reserved_rooms'])
            available_rooms = set(current_data[self.hotel_id]['available_rooms'])
        try:
            if room_number in reserved_rooms:
                reserved_rooms.discard(room_number)
                reserved_rooms = list(reserved_rooms)
                available_rooms.add(room_number)
                available_rooms = list(available_rooms)

                current_data[self.hotel_id]['reserved_rooms'] = reserved_rooms
                current_data[self.hotel_id]['available_rooms'] = available_rooms
            else:
                print("Room has been canceled before")
            with open(self.output_file, "w") as outfile:
                hotel_json = json.dumps(current_data)
                outfile.write(hotel_json)
        except KeyError:
            print("Hotel info couldn't be found on file")
