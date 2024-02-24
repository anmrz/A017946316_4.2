"""Class representing costumer"""
import json
import random
import string


class Costumer:
    """A class represents a Customer"""
    def __init__(self, name, phone, email, card_number):
        self.name = name
        self.phone = phone
        self.card_number = card_number
        self.email = email
        self.costumer_id = 'C' + ''.join(random.choices(string.digits, k=4))
        self.output_file = "costumer.json"

    def create_costumer(self):
        """Creates a costumer and registers in file"""
        costumer_data = {
                            'name': self.name,
                            'phone': self.phone,
                            'card': self.card_number,
                            'email': self.email}
        current_data = {}
        try:
            with open(self.output_file, "r") as outfile:
                current_data = json.load(outfile)
        except FileNotFoundError:
            pass
        current_data[self.costumer_id]=costumer_data 
        costumer_json = json.dumps(current_data)
        with open(self.output_file, "w") as outfile:
            outfile.write(costumer_json)

    def delete_costumer(self):
        """Deletes a customer"""
        try:
            with open(self.output_file, "r") as outfile:
                current_data = json.load(outfile)
                del current_data[self.costumer_id]
                costumer_json = json.dumps(current_data)
                with open(self.output_file, "w") as outfile:
                    outfile.write(costumer_json)
        except FileNotFoundError:
            print("File not found")
            raise
        except KeyError:
            print("Costumer does not exist in list")
            raise

    def display_costumer_info(self):
        """Shows customer info from file"""
        try:
            with open(self.output_file, "r") as outfile:
                current_data = json.load(outfile)
                return current_data[self.costumer_id]
        except FileNotFoundError:
            print("File not found")
            raise
        except KeyError:
            print("Costumer does not exist in file")
            raise

    def modify_costumer_info(self, phone,  email, card_number):
        """Modifies custome details: phone, email, card_number"""
        self.phone = phone
        self.card_number = card_number
        self.email = email
        new_data = {
                    'name': self.name,
                    'phone': self.phone,
                    'card': self.card_number,
                    'email': self.email}
        try:
            with open(self.output_file, "r") as outfile:
                current_data = json.load(outfile)
                current_data[self.costumer_id] = new_data
                costumer_json = json.dumps(current_data)
                with open(self.output_file, "w") as outfile:
                    outfile.write(costumer_json)
        except FileNotFoundError:
            raise
        except KeyError:
            print("Costumer does not exist in file")
            raise
  