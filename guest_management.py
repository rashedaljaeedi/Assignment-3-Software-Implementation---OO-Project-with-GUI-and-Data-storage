import os
import pickle


GUEST_FILE_PATH = "guests.bin"

class Guest:
    # Initializes a Guest object with personal contact details.
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id  # Unique identifier for the guest
        self.name = name  # Name of the guest
        self.address = address  # Address of the guest
        self.contact_details = contact_details  # Contact details for the guest

class GuestManagement:
    def __init__(self):
        self.guests = self.load_guests()

    def load_guests(self):
        if os.path.exists(GUEST_FILE_PATH):
            with open(GUEST_FILE_PATH, "rb") as file:
                return pickle.load(file)
        return {}

    def save_guests(self):
        with open(GUEST_FILE_PATH, "wb") as file:
            pickle.dump(self.guests, file)

    def add_guest(self, guest):
        if guest.guest_id in self.guests:
            raise Exception("Guest ID already exists.")
        self.guests[guest.guest_id] = guest
        self.save_guests()

    def delete_guest(self, guest_id):
        if guest_id not in self.guests:
            raise Exception("Guest not found.")
        del self.guests[guest_id]
        self.save_guests()

    def modify_guest(self, guest_id, **kwargs):
        if guest_id not in self.guests:
            raise Exception("Guest not found.")
        guest = self.guests[guest_id]
        for key, value in kwargs.items():
            if hasattr(guest, key):
                setattr(guest, key, value)
            else:
                raise Exception(f"{key} is not a valid attribute of Guest.")
        self.save_guests()

    def get_guest(self, guest_id):
        if guest_id not in self.guests:
            raise Exception("Guest not found.")
        return self.guests[guest_id]

    def display_guest(self, guest_id):
        guest = self.get_guest(guest_id)
        print(f"Guest ID: {guest.guest_id}")
        print(f"Name: {guest.name}")
        print(f"Address: {guest.address}")
        print(f"Contact Details: {guest.contact_details}")

    def display_all_guests(self):
        if not self.guests:
            return "No guests to display."
        else:
            all_guests_info = ""
            for guest_id, guest in self.guests.items():
                all_guests_info += f"Guest ID: {guest.guest_id}\n"
                all_guests_info += f"Name: {guest.name}\n"
                all_guests_info += f"Address: {guest.address}\n"
                all_guests_info += f"Contact Details: {guest.contact_details}\n\n"
            return all_guests_info

