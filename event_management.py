# event_management.py
import os
import pickle

EVENT_FILE_PATH = "events.bin"

class Event:
    # Initializes an Event object with details about the event.
    def __init__(
            self,
            event_id,
            event_type,
            theme,
            date,
            time,
            duration,
            venue_address,
            client_id,
            guest_list,
            catering_company,
            cleaning_company,
            decorations_company,
            entertainment_company,
            furniture_supply_company,
            invoice,
    ):
        self.event_id = event_id
        self.event_type = event_type  # Type of the event (e.g., wedding, conference)
        self.theme = theme  # Theme of the event
        self.date = date  # Date of the event
        self.time = time  # Time the event starts
        self.duration = duration  # Duration of the event
        self.venue_address = venue_address  # Address of the event venue
        self.client_id = client_id  # Client ID for whom the event is organized
        self.guest_list = guest_list  # List of guests attending the event
        # Companies providing various services for the event
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decorations_company = decorations_company
        self.entertainment_company = entertainment_company
        self.furniture_supply_company = furniture_supply_company
        self.invoice = invoice  # Invoice details for the event


class EventManagement:
    def __init__(self):
        self.events = self.load_events()

    def load_events(self):
        if os.path.exists(EVENT_FILE_PATH):
            with open(EVENT_FILE_PATH, "rb") as file:
                return pickle.load(file)
        return {}

    def save_events(self):
        with open(EVENT_FILE_PATH, "wb") as file:
            pickle.dump(self.events, file)

    def add_event(self, event):
        if event.event_id in self.events:
            raise Exception("Event ID already exists.")
        self.events[event.event_id] = event
        self.save_events()

    def delete_event(self, event_id):
        if event_id not in self.events:
            raise Exception("Event not found.")
        del self.events[event_id]
        self.save_events()

    def modify_event(self, event_id, **kwargs):
        if event_id not in self.events:
            raise Exception("Event not found.")
        event = self.events[event_id]
        for key, value in kwargs.items():
            if hasattr(event, key):
                setattr(event, key, value)
            else:
                raise Exception(f"{key} is not a valid attribute of Event.")
        self.save_events()

    def get_event(self, event_id):
        if event_id not in self.events:
            raise Exception("Event not found.")
        return self.events[event_id]

    def display_event(self, event_id):
        event = self.get_event(event_id)
        print(f"Event ID: {event.event_id}")
        print(f"Type: {event.event_type}")
        print(f"Theme: {event.theme}")
        print(f"Date: {event.date}")
        print(f"Time: {event.time}")
        print(f"Duration: {event.duration}")
        print(f"Venue Address: {event.venue_address}")
        print(f"Client ID: {event.client_id}")
        print("Guest List:")
        for guest in event.guest_list:
            print(f" - {guest}")
        print(f"Catering Company: {event.catering_company}")
        print(f"Cleaning Company: {event.cleaning_company}")
        print(f"Decorations Company: {event.decorations_company}")
        print(f"Entertainment Company: {event.entertainment_company}")
        print(f"Furniture Supply Company: {event.furniture_supply_company}")
        print(f"Invoice: {event.invoice}")


    def display_all_events(self):
        if not self.events:
            return "No events to display."
        else:
            all_events_info = ""
            for event_id, event in self.events.items():
                all_events_info += f"Event ID: {event.event_id}\n"
                all_events_info += f"Type: {event.event_type}\n"
                all_events_info += f"Theme: {event.theme}\n"
                all_events_info += f"Date: {event.date}\n"
                all_events_info += f"Time: {event.time}\n"
                all_events_info += f"Duration: {event.duration}\n"
                all_events_info += f"Venue Address: {event.venue_address}\n"
                all_events_info += f"Client ID: {event.client_id}\n"
                all_events_info += f"Catering Company: {event.catering_company}\n"
                all_events_info += f"Cleaning Company: {event.cleaning_company}\n"
                all_events_info += f"Decorations Company: {event.decorations_company}\n"
                all_events_info += f"Guest List: {event.guest_list}\n"
                all_events_info += f"Entertainment Company: {event.entertainment_company}\n"
                all_events_info += f"Furniture Supply Company: {event.furniture_supply_company}\n"
                all_events_info += f"Invoice: {event.invoice}\n\n"
            return all_events_info
