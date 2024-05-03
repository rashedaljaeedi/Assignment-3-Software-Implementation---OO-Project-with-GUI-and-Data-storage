import os  # Importing the os module for operating system related functionalities
import pickle  # Importing the pickle module for object serialization

EVENT_FILE_PATH = "events.bin"  # File path constant for storing event data

class Event:  # Definition of the Event class
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, cleaning_company, decorations_company, entertainment_company, furniture_supply_company, invoice):  # Constructor method for initializing event attributes
        self.event_id = event_id  # Assigning event ID
        self.event_type = event_type  # Assigning event type
        self.theme = theme  # Assigning event theme
        self.date = date  # Assigning event date
        self.time = time  # Assigning event time
        self.duration = duration  # Assigning event duration
        self.venue_address = venue_address  # Assigning event venue address
        self.client_id = client_id  # Assigning client ID for the event
        self.guest_list = guest_list  # Assigning event guest list
        self.catering_company = catering_company  # Assigning catering company for the event
        self.cleaning_company = cleaning_company  # Assigning cleaning company for the event
        self.decorations_company = decorations_company  # Assigning decorations company for the event
        self.entertainment_company = entertainment_company  # Assigning entertainment company for the event
        self.furniture_supply_company = furniture_supply_company  # Assigning furniture supply company for the event
        self.invoice = invoice  # Assigning invoice details for the event

class EventManagement:  # Definition of the EventManagement class
    def __init__(self):  # Constructor method for initializing event management instance
        self.events = self.load_events()  # Loading events data when an instance is created

    def load_events(self):  # Method for loading events data from file
        """
        Load events from the binary file if it exists.
        Returns:
            dict: A dictionary containing loaded event data.
        """
        if os.path.exists(EVENT_FILE_PATH):  # Checking if the file exists
            with open(EVENT_FILE_PATH, "rb") as file:  # Opening the file in binary read mode
                try:
                    return pickle.load(file)  # Loading data from the file using pickle
                except (pickle.UnpicklingError, EOFError) as e:  # Handling errors during unpickling
                    print(f"Error loading events data: {e}")  # Printing error message
                    return {}  # Returning an empty dictionary if error occurs
        return {}  # Returning an empty dictionary if file doesn't exist

    def save_events(self):  # Method for saving events data to file
        with open(EVENT_FILE_PATH, "wb") as file:  # Opening the file in binary write mode
            pickle.dump(self.events, file)  # Saving data to the file using pickle

    def add_event(self, event):  # Method for adding a new event
        if event.event_id in self.events:  # Checking if event ID already exists
            raise ValueError("Event ID already exists.")  # Raising an error if event ID is not unique
        self.events[event.event_id] = event  # Adding the new event to the events dictionary
        self.save_events()  # Saving the updated events data to file

    def delete_event(self, event_id):  # Method for deleting an event
        if event_id not in self.events:  # Checking if event ID exists
            raise ValueError("Event not found.")  # Raising an error if event ID doesn't exist
        del self.events[event_id]  # Deleting the event from the events dictionary
        self.save_events()  # Saving the updated events data to file

    def modify_event(self, event_id, **kwargs):  # Method for modifying event attributes
        if event_id not in self.events:  # Checking if event ID exists
            raise ValueError("Event not found.")  # Raising an error if event ID doesn't exist
        event = self.events[event_id]  # Getting the event object
        allowed_attributes = set(['event_type', 'theme', 'date', 'time', 'duration', 'venue_address', 'client_id', 'guest_list', 'catering_company', 'cleaning_company', 'decorations_company', 'entertainment_company', 'furniture_supply_company', 'invoice'])  # Allowed attributes for modification
        for key, value in kwargs.items():  # Iterating over keyword arguments
            if key not in allowed_attributes:  # Checking if attribute is allowed for modification
                raise ValueError(f"{key} is not a valid attribute of Event.")  # Raising an error for invalid attribute
            setattr(event, key, value)  # Setting the new value for the attribute
        self.save_events()  # Saving the updated events data to file

    def get_event(self, event_id):  # Method for retrieving an event
        if event_id not in self.events:  # Checking if event ID exists
            raise ValueError("Event not found.")  # Raising an error if event ID doesn't exist
        return self.events[event_id]  # Returning the event object

    def display_event(self, event_id):  # Method for displaying details of a specific event
        event = self.get_event(event_id)  # Getting the event object
        print(f"Event ID: {event.event_id}")  # Displaying event ID
        print(f"Type: {event.event_type}")  # Displaying event type
        print(f"Theme: {event.theme}")  # Displaying event theme
        print(f"Date: {event.date}")  # Displaying event date
        print(f"Time: {event.time}")  # Displaying event time
        print(f"Duration: {event.duration}")  # Displaying event duration
        print(f"Venue Address: {event.venue_address}")  # Displaying event venue address
        print(f"Client ID: {event.client_id}")  # Displaying client ID for the event
        print("Guest List:")  # Displaying event guest list
        for guest in event.guest_list:  # Iterating over event guest list
            print(f" - {guest}")  # Displaying each guest
        print(f"Catering Company: {event.catering_company}")  # Displaying catering company for the event
        print(f"Cleaning Company: {event.cleaning_company}")  # Displaying cleaning company for the event
        print(f"Decorations Company: {event.decorations_company}")  # Displaying decorations company for the event
        print(f"Entertainment Company: {event.entertainment_company}")  # Displaying entertainment company for the event
        print(f"Furniture Supply Company: {event.furniture_supply_company}")  # Displaying furniture supply company for the event
        print(f"Invoice: {event.invoice}")  # Displaying invoice details for the event

    def display_all_events(self):  # Method for displaying details of all events
        if not self.events:  # Checking if events dictionary is empty
            return "No events to display."  # Returning message if no events exist
        else:
            all_events_info = ""  # Initializing string to store all events' information
            for event_id, event in self.events.items():  # Iterating over events dictionary
                all_events_info += f"Event ID: {event_id}\n"  # Adding event ID to the string
                all_events_info += f"Type: {event.event_type}\n"  # Adding event type to the string
                all_events_info += f"Theme: {event.theme}\n"  # Adding event theme to the string
                all_events_info += f"Date: {event.date}\n"  # Adding event date to the string
                all_events_info += f"Time: {event.time}\n"  # Adding event time to the string
                all_events_info += f"Duration: {event.duration}\n"  # Adding event duration to the string
                all_events_info += f"Venue Address: {event.venue_address}\n"  # Adding event venue address to the string
                all_events_info += f"Client ID: {event.client_id}\n"  # Adding client ID for the event to the string
                all_events_info += f"Guest List: {event.guest_list}\n"  # Adding event guest list to the string
                all_events_info += f"Catering Company: {event.catering_company}\n"  # Adding catering company for the event to the string
                all_events_info += f"Cleaning Company: {event.cleaning_company}\n"  # Adding cleaning company for the event to the string
                all_events_info += f"Decorations Company: {event.decorations_company}\n"  # Adding decorations company for the event to the string
                all_events_info += f"Entertainment Company: {event.entertainment_company}\n"  # Adding entertainment company for the event to the string
                all_events_info += f"Furniture Supply Company: {event.furniture_supply_company}\n"  # Adding furniture supply company for the event to the string
                all_events_info += f"Invoice: {event.invoice}\n\n"  # Adding invoice details for the event to the string
            return all_events_info  # Returning the string containing all events' information
