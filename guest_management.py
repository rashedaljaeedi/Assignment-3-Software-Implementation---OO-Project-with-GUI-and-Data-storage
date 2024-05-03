import os  # Importing the os module for operating system related functionalities
import pickle  # Importing the pickle module for object serialization

GUEST_FILE_PATH = "guests.bin"  # File path constant for storing guest data

class Guest:  # Definition of the Guest class
    # Initializes a Guest object with personal contact details.
    def __init__(self, guest_id, name, address, contact_details):  # Constructor method for initializing guest attributes
        self.guest_id = guest_id  # Unique identifier for the guest
        self.name = name  # Name of the guest
        self.address = address  # Address of the guest
        self.contact_details = contact_details  # Contact details for the guest

class GuestManagement:  # Definition of the GuestManagement class
    def __init__(self):  # Constructor method for initializing guest management instance
        self.guests = self.load_guests()  # Loading guests data when an instance is created

    def load_guests(self):  # Method for loading guests data from file
        """
        Load guests from the binary file if it exists.
        Returns:
            dict: A dictionary containing loaded guest data.
        """
        if os.path.exists(GUEST_FILE_PATH):  # Checking if the file exists
            with open(GUEST_FILE_PATH, "rb") as file:  # Opening the file in binary read mode
                try:
                    return pickle.load(file)  # Loading data from the file using pickle
                except (pickle.UnpicklingError, EOFError) as e:  # Handling errors during unpickling
                    print(f"Error loading guests data: {e}")  # Printing error message
                    return {}  # Returning an empty dictionary if error occurs
        return {}  # Returning an empty dictionary if file doesn't exist

    def save_guests(self):  # Method for saving guests data to file
        with open(GUEST_FILE_PATH, "wb") as file:  # Opening the file in binary write mode
            pickle.dump(self.guests, file)  # Saving data to the file using pickle

    def add_guest(self, guest):  # Method for adding a new guest
        if guest.guest_id in self.guests:  # Checking if guest ID already exists
            raise ValueError("Guest ID already exists.")  # Raising an error if guest ID is not unique
        self.guests[guest.guest_id] = guest  # Adding the new guest to the guests dictionary
        self.save_guests()  # Saving the updated guests data to file

    def delete_guest(self, guest_id):  # Method for deleting a guest
        if guest_id not in self.guests:  # Checking if guest ID exists
            raise ValueError("Guest not found.")  # Raising an error if guest ID doesn't exist
        del self.guests[guest_id]  # Deleting the guest from the guests dictionary
        self.save_guests()  # Saving the updated guests data to file

    def modify_guest(self, guest_id, **kwargs):  # Method for modifying guest attributes
        if guest_id not in self.guests:  # Checking if guest ID exists
            raise ValueError("Guest not found.")  # Raising an error if guest ID doesn't exist
        guest = self.guests[guest_id]  # Getting the guest object
        allowed_attributes = set(['name', 'address', 'contact_details'])  # Allowed attributes for modification
        for key, value in kwargs.items():  # Iterating over keyword arguments
            if key not in allowed_attributes:  # Checking if attribute is allowed for modification
                raise ValueError(f"{key} is not a valid attribute of Guest.")  # Raising an error for invalid attribute
            setattr(guest, key, value)  # Setting the new value for the attribute
        self.save_guests()  # Saving the updated guests data to file

    def get_guest(self, guest_id):  # Method for retrieving a guest
        if guest_id not in self.guests:  # Checking if guest ID exists
            raise ValueError("Guest not found.")  # Raising an error if guest ID doesn't exist
        return self.guests[guest_id]  # Returning the guest object

    def display_guest(self, guest_id):  # Method for displaying details of a specific guest
        guest = self.get_guest(guest_id)  # Getting the guest object
        print(f"Guest ID: {guest.guest_id}")  # Displaying guest ID
        print(f"Name: {guest.name}")  # Displaying guest name
        print(f"Address: {guest.address}")  # Displaying guest address
        print(f"Contact Details: {guest.contact_details}")  # Displaying guest contact details

    def display_all_guests(self):  # Method for displaying details of all guests
        if not self.guests:  # Checking if guests dictionary is empty
            return "No guests to display."  # Returning message if no guests exist
        else:
            all_guests_info = ""  # Initializing string to store all guests' information
            for guest_id, guest in self.guests.items():  # Iterating over guests dictionary
                all_guests_info += f"Guest ID: {guest_id}\n"  # Adding guest ID to the string
                all_guests_info += f"Name: {guest.name}\n"  # Adding guest name to the string
                all_guests_info += f"Address: {guest.address}\n"  # Adding guest address to the string
                all_guests_info += f"Contact Details: {guest.contact_details}\n\n"  # Adding guest contact details to the string
            return all_guests_info  # Returning the string containing all guests' information
