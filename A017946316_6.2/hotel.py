from datetime import date

class Hotel:
    def __init__(self):
        self.rooms = {}
        self.available_rooms = {'std' : [101, 102, 103], 'suite' : [201, 202, 203]}
        self.room_price = {1:2000, 2:6000}

    def create_reservation(self, name, address, phone):
        room_type = int(input('Room types: \n1.standard \n2.suite\nSelect a room type: '))
        if room_type == 1:
            if self.available_rooms['std']:
                room_number = self.available_rooms['std'].pop(0)
            else:
                print('sorry, standard rooms are not available')
        elif room_type == 2:
            if self.available_rooms['suite']:
                room_number = self.available_rooms['suite'].pop(0)
            else:
                print('sorry, suites are not available')
        else:
            print('Choose a valide room type')

        day, month, year = map(int, input('Enter check-in-date in day, month, year format').split())
        check_in = date(year, month, day)
        self.rooms[room_number] = {
            'name' : name,
            'address' : address,
            'phone' : phone,
            'check_in_date' : check_in,
            'room_type' : room_type,
        }
        print(f"Reserved for {name}, {address} to room, {room_number} on {check_in}")


    def cancel_reservation(self, room_number):
        pass

    def display_occupied(self):
        pass

    def start_app(self):
        while True:
            print("--------------------")
            print("1. Reserve")
            print("2. Display occupied Rooms")
            print("4. Cancel Reservation")
            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                name = input("Enter Client Name: ")
                address = input("Enter Address: ")
                phone = input("Enter Contact Phone: ")
                self.create_reservation(name, address, phone)
            elif choice == "2":
                self.display_occupied()
            elif choice == "4":
                room_number = int(input("Enter room number:  "))
                self.cancel_reservation(room_number)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again")

h = Hotel()
h.start_app()
