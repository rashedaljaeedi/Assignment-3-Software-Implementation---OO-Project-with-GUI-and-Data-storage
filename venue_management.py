import os  # Importing the os module for operating system related functionalities
import pickle  # Importing the pickle module for object serialization

VENUE_FILE_PATH = "venues.bin"  # File path constant for storing venue data

class Venue:  # Definition of the Venue class
    # Initializes a Venue object with location and capacity details.
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id  # Unique identifier for the venue
        self.name = name  # Name of the venue
        self.address = address  # Address of the venue
        self.contact = contact  # Contact information for the venue
        self.min_guests = min_guests  # Minimum number of guests the venue can accommodate
        self.max_guests = max_guests  # Maximum number of guests the venue can accommodate

class VenueManagement:  # Definition of the VenueManagement class
    def __init__(self):  # Constructor method for initializing venue management instance
        self.venues = self.load_venues()  # Loading venues data when an instance is created

    def load_venues(self):  # Method for loading venues data from file
        if os.path.exists(VENUE_FILE_PATH):  # Checking if the file exists
            with open(VENUE_FILE_PATH, "rb") as file:  # Opening the file in binary read mode
                try:
                    return pickle.load(file)  # Loading data from the file using pickle
                except (pickle.UnpicklingError, EOFError) as e:  # Handling errors during unpickling
                    print(f"Error loading venues data: {e}")  # Printing error message
                    return {}  # Returning an empty dictionary if error occurs
        return {}  # Returning an empty dictionary if file doesn't exist

    def save_venues(self):  # Method for saving venues data to file
        with open(VENUE_FILE_PATH, "wb") as file:  # Opening the file in binary write mode
            pickle.dump(self.venues, file)  # Saving data to the file using pickle

    def add_venue(self, venue):  # Method for adding a new venue
        if venue.venue_id in self.venues:  # Checking if venue ID already exists
            raise Exception("Venue ID already exists.")  # Raising an error if venue ID is not unique
        self.venues[venue.venue_id] = venue  # Adding the new venue to the venues dictionary
        self.save_venues()  # Saving the updated venues data to file

    def delete_venue(self, venue_id):  # Method for deleting a venue
        if venue_id not in self.venues:  # Checking if venue ID exists
            raise Exception("Venue not found.")  # Raising an error if venue ID doesn't exist
        del self.venues[venue_id]  # Deleting the venue from the venues dictionary
        self.save_venues()  # Saving the updated venues data to file

    def modify_venue(self, venue_id, **kwargs):  # Method for modifying venue attributes
        if venue_id not in self.venues:  # Checking if venue ID exists
            raise Exception("Venue not found.")  # Raising an error if venue ID doesn't exist
        venue = self.venues[venue_id]  # Getting the venue object
        for key, value in kwargs.items():  # Iterating over keyword arguments
            if hasattr(venue, key):  # Checking if the venue has the attribute
                setattr(venue, key, value)  # Setting the new value for the attribute
            else:
                raise Exception(f"{key} is not a valid attribute of Venue.")  # Raising an error for invalid attribute
        self.save_venues()  # Saving the updated venues data to file

    def get_venue(self, venue_id):  # Method for retrieving a venue
        if venue_id not in self.venues:  # Checking if venue ID exists
            raise Exception("Venue not found.")  # Raising an error if venue ID doesn't exist
        return self.venues[venue_id]  # Returning the venue object

    def display_venue(self, venue_id):  # Method for displaying details of a specific venue
        venue = self.get_venue(venue_id)  # Getting the venue object
        print(f"Venue ID: {venue.venue_id}")  # Displaying venue ID
        print(f"Name: {venue.name}")  # Displaying venue name
        print(f"Address: {venue.address}")  # Displaying venue address
        print(f"Contact: {venue.contact}")  # Displaying venue contact
        print(f"Minimum Guests: {venue.min_guests}")  # Displaying minimum guests
        print(f"Maximum Guests: {venue.max_guests}")  # Displaying maximum guests

    def display_all_venues(self):  # Method for displaying details of all venues
        if not self.venues:  # Checking if venues dictionary is empty
            return "No venues to display."  # Returning message if no venues exist
        else:
            all_venues_info = ""  # Initializing string to store all venues' information
            for venue_id, venue in self.venues.items():  # Iterating over venues dictionary
                all_venues_info += f"Venue ID: {venue_id}\n"  # Adding venue ID to the string
                all_venues_info += f"Name: {venue.name}\n"  # Adding venue name to the string
                all_venues_info += f"Address: {venue.address}\n"  # Adding venue address to the string
                all_venues_info += f"Contact: {venue.contact}\n"  # Adding venue contact to the string
                all_venues_info += f"Minimum Guests: {venue.min_guests}\n"  # Adding minimum guests to the string
                all_venues_info += f"Maximum Guests: {venue.max_guests}\n\n"  # Adding maximum guests to the string
            return all_venues_info  # Returning the string containing all venues' information
