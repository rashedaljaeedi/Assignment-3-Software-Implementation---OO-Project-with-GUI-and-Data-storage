# venue_management.py
import os
import pickle

VENUE_FILE_PATH = "venues.bin"

class Venue:
    # Initializes a Venue object with location and capacity details.
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id  # Unique identifier for the venue
        self.name = name  # Name of the venue
        self.address = address  # Address of the venue
        self.contact = contact  # Contact information for the venue
        self.min_guests = min_guests  # Minimum number of guests the venue can accommodate
        self.max_guests = max_guests  # Maximum number of guests the venue can accommodate


class VenueManagement:
    def __init__(self):
        self.venues = self.load_venues()

    def load_venues(self):
        if os.path.exists(VENUE_FILE_PATH):
            with open(VENUE_FILE_PATH, "rb") as file:
                return pickle.load(file)
        return {}

    def save_venues(self):
        with open(VENUE_FILE_PATH, "wb") as file:
            pickle.dump(self.venues, file)

    def add_venue(self, venue):
        if venue.venue_id in self.venues:
            raise Exception("Venue ID already exists.")
        self.venues[venue.venue_id] = venue
        self.save_venues()

    def delete_venue(self, venue_id):
        if venue_id not in self.venues:
            raise Exception("Venue not found.")
        del self.venues[venue_id]
        self.save_venues()

    def modify_venue(self, venue_id, **kwargs):
        if venue_id not in self.venues:
            raise Exception("Venue not found.")
        venue = self.venues[venue_id]
        for key, value in kwargs.items():
            if hasattr(venue, key):
                setattr(venue, key, value)
            else:
                raise Exception(f"{key} is not a valid attribute of Venue.")
        self.save_venues()

    def get_venue(self, venue_id):
        if venue_id not in self.venues:
            raise Exception("Venue not found.")
        return self.venues[venue_id]

    def display_venue(self, venue_id):
        venue = self.get_venue(venue_id)
        print(f"Venue ID: {venue.venue_id}")
        print(f"Name: {venue.name}")
        print(f"Address: {venue.address}")
        print(f"Contact: {venue.contact}")
        print(f"Minimum Guests: {venue.min_guests}")
        print(f"Maximum Guests: {venue.max_guests}")

    def display_all_venues(self):
        if not self.venues:
            return "No venues to display."
        else:
            all_venues_info = ""
            for venue_id, venue in self.venues.items():
                all_venues_info += f"Venue ID: {venue.venue_id}\n"
                all_venues_info += f"Name: {venue.name}\n"
                all_venues_info += f"Address: {venue.address}\n"
                all_venues_info += f"Contact: {venue.contact}\n"
                all_venues_info += f"Minimum Guests: {venue.min_guests}\n"
                all_venues_info += f"Maximum Guests: {venue.max_guests}\n\n"
            return all_venues_info








