import tkinter as tk  # Importing the tkinter module and aliasing it as tk
import pickle  # Importing the pickle module
from tkinter import ttk  # Importing the ttk submodule from tkinter
from tkinter import messagebox  # Importing the messagebox submodule from tkinter
from event_management import Event, EventManagement  # Importing Event and EventManagement classes from
# event_management module
from guest_management import Guest, GuestManagement  # Importing Guest and GuestManagement classes from guest_management module
from supplier_management import Supplier, SupplierManagement  # Importing Supplier and SupplierManagement classes from supplier_management module
from venue_management import Venue, VenueManagement  # Importing Venue and VenueManagement classes from venue_management module
from client_management import Client, ClientManagement  # Importing Client and ClientManagement classes from client_management module
from employee_management import Employee, EmployeeManagement  # Importing Employee and EmployeeManagement classes from employee_management module


class EventGUI:
    def __init__(self, master):  # Constructor method for EventGUI class, taking master as an argument
        self.master = master  # Assigning the master argument to the master attribute
        self.event_management = EventManagement()  # Creating an instance of EventManagement and assigning it to event_management attribute
        self.create_widgets()  # Calling the create_widgets method to create GUI elements

    def create_widgets(self):  # Method to create GUI elements
        # Widgets for event management GUI
        labels = [  # Creating a list of labels
            "Event ID:",  # Label for Event ID
            "Type:",  # Label for Type
            "Theme:",  # Label for Theme
            "Date:",  # Label for Date
            "Time:",  # Label for Time
            "Duration:",  # Label for Duration
            "Venue Address:",  # Label for Venue Address
            "Client ID:",  # Label for Client ID
            "Catering Company:",  # Label for Catering Company
            "Cleaning Company:",  # Label for Cleaning Company
            "Decorations Company:",  # Label for Decorations Company
            "Guest List",  # Label for Guest List
            "Entertainment Company",  # Label for Entertainment Company
            "Furniture Company",  # Label for Furniture Company
            "Invoice",  # Label for Invoice
        ]
        self.entries = {}  # Creating an empty dictionary to store entry widgets
        for i, label in enumerate(labels):  # Iterating over labels
            tk.Label(self.master, text=label).grid(row=i, column=0, sticky="w")  # Creating label widgets and placing them in the grid
            entry = tk.Entry(self.master)  # Creating entry widgets
            entry.grid(row=i, column=1, sticky="we")  # Placing entry widgets in the grid
            self.entries[label.strip(":")] = entry  # Adding entry widgets to the dictionary with label as the key

        operations = [  # Creating a list of operations
            ("Add Event", self.add_event),  # Add Event operation
            ("Delete Event", self.delete_event),  # Delete Event operation
            ("Modify Event", self.modify_event),  # Modify Event operation
            ("Display Event", self.display_event),  # Display Event operation
            ("Display All Events", self.display_all_events)  # Display All Events operation
        ]
        for i, (text, command) in enumerate(operations, start=len(labels)):  # Iterating over operations
            button = tk.Button(self.master, text=text, command=command)  # Creating button widgets
            button.grid(row=i, columnspan=2, sticky="we")  # Placing button widgets in the grid


    def add_event(self):  # Method to add an event
        try:  # Starting a try block
            event_data = {key: entry.get() for key, entry in self.entries.items()}  # Creating a dictionary of event data from entry widgets

            event_data["event_id"] = event_data.pop("Event ID")  # Changing "Event ID" key to "event_id"
            event_data["event_type"] = event_data.pop("Type")  # Changing "Type" key to "event_type"
            event_data["theme"] = event_data.pop("Theme")  # Changing "Theme" key to "theme"
            event_data["date"] = event_data.pop("Date")  # Changing "Date" key to "date"
            event_data["time"] = event_data.pop("Time")  # Changing "Time" key to "time"
            event_data["duration"] = event_data.pop("Duration")  # Changing "Duration" key to "duration"
            event_data["venue_address"] = event_data.pop("Venue Address")  # Changing "Venue Address" key to "venue_address"
            event_data["client_id"] = event_data.pop("Client ID")  # Changing "Client ID" key to "client_id"
            event_data["catering_company"] = event_data.pop("Catering Company")  # Changing "Catering Company" key to "catering_company"
            event_data["cleaning_company"] = event_data.pop("Cleaning Company")  # Changing "Cleaning Company" key to "cleaning_company"
            event_data["decorations_company"] = event_data.pop("Decorations Company")  # Changing "Decorations Company" key to "decorations_company"
            event_data["guest_list"] = event_data.pop("Guest List")  # Changing "Guest List" key to "guest_list"
            event_data["entertainment_company"] = event_data.pop("Entertainment Company")  # Changing "Entertainment Company" key to "entertainment_company"
            event_data["furniture_supply_company"] = event_data.pop("Furniture Company")  # Changing "Furniture Company" key to "furniture_supply_company"
            event_data["invoice"] = event_data.pop("Invoice")  # Changing "Invoice" key to "invoice"

            new_event = Event(**event_data)  # Creating a new Event instance with event data
            self.event_management.add_event(new_event)  # Adding the new event to event management
            messagebox.showinfo("Success", "Event added successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not add event: {e}")  # Displaying error message

    def delete_event(self):  # Method to delete an event
        event_id = self.entries["Event ID"].get()  # Getting the event ID from entry widget
        try:  # Starting a try block
            self.event_management.delete_event(event_id)  # Deleting the event
            messagebox.showinfo("Success", "Event deleted successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not delete event: {e}")  # Displaying error message

    def modify_event(self):  # Method to modify an event
        event_id = self.entries["Event ID"].get()  # Getting the event ID from entry widget
        updates = {  # Creating a dictionary of updates
            key: entry.get() for key, entry in self.entries.items() if entry.get()  # Getting updates from entry widgets
        }
        try:  # Starting a try block
            self.event_management.modify_event(event_id, **updates)  # Modifying the event
            messagebox.showinfo("Success", "Event modified successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not modify event: {e}")  # Displaying error message

    def display_event(self):  # Method to display an event
        event_id = self.entries["Event ID"].get()  # Getting the event ID from entry widget
        try:  # Starting a try block
            event = self.event_management.get_event(event_id)  # Getting the event
            event_info = "\n".join(  # Joining event information into a string
                f"{key}: {getattr(event, key.lower().replace(' ', '_'), '')}"  # Formatting each line of event information
                if key != "Type"  # Ensure event type is excluded from here
                else f"{key}: {event.event_type}"  # Displaying event type separately
                for key in self.entries
            )
            messagebox.showinfo("Event Details", event_info)  # Displaying event information
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not display event: {e}")  # Displaying error message

    def display_all_events(self):  # Method to display all events
        try:  # Starting a try block
            all_events_info = self.event_management.display_all_events()  # Getting information of all events
            if all_events_info:  # Checking if there are events to display
                messagebox.showinfo("All Events Details", all_events_info)  # Displaying all events information
            else:  # If there are no events to display
                messagebox.showinfo("All Events Details", "No events to display.")  # Displaying message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", str(e))  # Displaying error message
class GuestGUI:
    def __init__(self, master):  # Constructor method for GuestGUI class, taking master as an argument
        self.master = master  # Assigning the master argument to the master attribute
        self.guest_management = GuestManagement()  # Creating an instance of GuestManagement and assigning it to guest_management attribute
        self.create_widgets()  # Calling the create_widgets method to create GUI elements

    def create_widgets(self):  # Method to create GUI elements
        # Guest ID
        tk.Label(self.master, text="Guest ID:").grid(row=0, column=0, sticky="w")  # Creating label widget for Guest ID
        self.guest_id_entry = tk.Entry(self.master)  # Creating entry widget for Guest ID
        self.guest_id_entry.grid(row=0, column=1, sticky="we")  # Placing entry widget in the grid

        # Name
        tk.Label(self.master, text="Name:").grid(row=1, column=0, sticky="w")  # Creating label widget for Name
        self.name_entry = tk.Entry(self.master)  # Creating entry widget for Name
        self.name_entry.grid(row=1, column=1, sticky="we")  # Placing entry widget in the grid

        # Address
        tk.Label(self.master, text="Address:").grid(row=2, column=0, sticky="w")  # Creating label widget for Address
        self.address_entry = tk.Entry(self.master)  # Creating entry widget for Address
        self.address_entry.grid(row=2, column=1, sticky="we")  # Placing entry widget in the grid

        # Contact Details
        tk.Label(self.master, text="Contact Details:").grid(row=3, column=0, sticky="w")  # Creating label widget for Contact Details
        self.contact_details_entry = tk.Entry(self.master)  # Creating entry widget for Contact Details
        self.contact_details_entry.grid(row=3, column=1, sticky="we")  # Placing entry widget in the grid

        # Buttons for operations
        self.add_button = tk.Button(  # Creating button widget for adding a guest
            self.master, text="Add Guest", command=self.add_guest  # Assigning text and command to the button
        )
        self.add_button.grid(row=4, column=0, sticky="we")  # Placing button widget in the grid

        self.delete_button = tk.Button(  # Creating button widget for deleting a guest
            self.master, text="Delete Guest", command=self.delete_guest  # Assigning text and command to the button
        )
        self.delete_button.grid(row=4, column=1, sticky="we")  # Placing button widget in the grid

        self.modify_button = tk.Button(  # Creating button widget for modifying a guest
            self.master, text="Modify Guest", command=self.modify_guest  # Assigning text and command to the button
        )
        self.modify_button.grid(row=5, column=0, sticky="we")  # Placing button widget in the grid

        self.display_button = tk.Button(  # Creating button widget for displaying a guest
            self.master, text="Display Guest", command=self.display_guest  # Assigning text and command to the button
        )
        self.display_button.grid(row=5, column=1, sticky="we")  # Placing button widget in the grid

        self.display_all_button = tk.Button(  # Creating button widget for displaying all guests
            self.master, text="Display All Guests", command=self.display_all_guests  # Assigning text and command to the button
        )
        self.display_all_button.grid(row=6, column=0, columnspan=2, sticky="we")  # Placing button widget in the grid

    def add_guest(self):  # Method to add a guest
        guest_id = self.guest_id_entry.get()  # Getting guest ID from entry widget
        name = self.name_entry.get()  # Getting guest name from entry widget
        address = self.address_entry.get()  # Getting guest address from entry widget
        contact_details = self.contact_details_entry.get()  # Getting guest contact details from entry widget
        try:  # Starting a try block
            new_guest = Guest(guest_id, name, address, contact_details)  # Creating a new Guest instance
            self.guest_management.add_guest(new_guest)  # Adding the new guest
            messagebox.showinfo("Success", "Guest added successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not add guest: {e}")  # Displaying error message

    def delete_guest(self):  # Method to delete a guest
        guest_id = self.guest_id_entry.get()  # Getting guest ID from entry widget
        try:  # Starting a try block
            self.guest_management.delete_guest(guest_id)  # Deleting the guest
            messagebox.showinfo("Success", "Guest deleted successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not delete guest: {e}")  # Displaying error message

    def modify_guest(self):  # Method to modify a guest
        guest_id = self.guest_id_entry.get()  # Getting guest ID from entry widget
        name = self.name_entry.get()  # Getting guest name from entry widget
        address = self.address_entry.get()  # Getting guest address from entry widget
        contact_details = self.contact_details_entry.get()  # Getting guest contact details from entry widget
        try:  # Starting a try block
            self.guest_management.modify_guest(  # Modifying the guest
                guest_id, name=name, address=address, contact_details=contact_details
            )
            messagebox.showinfo("Success", "Guest modified successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not modify guest: {e}")  # Displaying error message

    def display_guest(self):  # Method to display a guest
        guest_id = self.guest_id_entry.get()  # Getting guest ID from entry widget
        try:  # Starting a try block
            guest = self.guest_management.get_guest(guest_id)  # Getting the guest
            guest_info = f"Guest ID: {guest.guest_id}\nName: {guest.name}\nAddress: {guest.address}\nContact Details: {guest.contact_details}"  # Formatting guest information
            messagebox.showinfo("Guest Details", guest_info)  # Displaying guest information
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not display guest: {e}")  # Displaying error message

    def display_all_guests(self):  # Method to display all guests
        try:  # Starting a try block
            all_guests_info = self.guest_management.display_all_guests()  # Getting information of all guests
            if all_guests_info:  # Checking if there are guests to display
                messagebox.showinfo("All Guests Details", all_guests_info)  # Displaying all guests information
            else:  # If there are no guests to display
                messagebox.showinfo("All Guests Details", "No guests to display.")  # Displaying message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", str(e))  # Displaying error message


class SupplierGUI:
    def __init__(self, master):  # Constructor method for SupplierGUI class, taking master as an argument
        self.master = master  # Assigning the master argument to the master attribute
        self.supplier_management = SupplierManagement()  # Creating an instance of SupplierManagement and assigning it to supplier_management attribute
        self.create_widgets()  # Calling the create_widgets method to create GUI elements

    def create_widgets(self):  # Method to create GUI elements
        # Supplier ID
        tk.Label(self.master, text="Supplier ID:").grid(row=0, column=0, sticky="w")  # Creating label widget for Supplier ID
        self.supplier_id_entry = tk.Entry(self.master)  # Creating entry widget for Supplier ID
        self.supplier_id_entry.grid(row=0, column=1, sticky="we")  # Placing entry widget in the grid

        # Name
        tk.Label(self.master, text="Name:").grid(row=1, column=0, sticky="w")  # Creating label widget for Name
        self.name_entry = tk.Entry(self.master)  # Creating entry widget for Name
        self.name_entry.grid(row=1, column=1, sticky="we")  # Placing entry widget in the grid

        # Address
        tk.Label(self.master, text="Address:").grid(row=2, column=0, sticky="w")  # Creating label widget for Address
        self.address_entry = tk.Entry(self.master)  # Creating entry widget for Address
        self.address_entry.grid(row=2, column=1, sticky="we")  # Placing entry widget in the grid

        # Contact Details
        tk.Label(self.master, text="Contact Details:").grid(row=3, column=0, sticky="w")  # Creating label widget for Contact Details
        self.contact_details_entry = tk.Entry(self.master)  # Creating entry widget for Contact Details
        self.contact_details_entry.grid(row=3, column=1, sticky="we")  # Placing entry widget in the grid

        # Service Provided
        tk.Label(self.master, text="Service Provided:").grid(row=4, column=0, sticky="w")  # Creating label widget for Service Provided
        self.service_provided_entry = tk.Entry(self.master)  # Creating entry widget for Service Provided
        self.service_provided_entry.grid(row=4, column=1, sticky="we")  # Placing entry widget in the grid

        # Min Guests
        tk.Label(self.master, text="Min Guests:").grid(row=5, column=0, sticky="w")  # Creating label widget for Min Guests
        self.min_guests_supplier_entry = tk.Entry(self.master)  # Creating entry widget for Min Guests
        self.min_guests_supplier_entry.grid(row=5, column=1, sticky="we")  # Placing entry widget in the grid

        # Max Guests
        tk.Label(self.master, text="Max Guests:").grid(row=6, column=0, sticky="w")  # Creating label widget for Max Guests
        self.max_guests_supplier_entry = tk.Entry(self.master)  # Creating entry widget for Max Guests
        self.max_guests_supplier_entry.grid(row=6, column=1, sticky="we")  # Placing entry widget in the grid

        # menu
        tk.Label(self.master, text="Menu:").grid(row=7, column=0, sticky="w")  # Creating label widget for menu
        self.menu_entry = tk.Entry(self.master)  # Creating entry widget for menu
        self.menu_entry.grid(row=7, column=1, sticky="we")  # Placing entry widget in the grid

        # Buttons for operations
        self.add_button = tk.Button(  # Creating button widget for adding a supplier
            self.master, text="Add Supplier", command=self.add_supplier  # Assigning text and command to the button
        )
        self.add_button.grid(row=8, column=0, sticky="we")  # Placing button widget in the grid

        self.delete_button = tk.Button(  # Creating button widget for deleting a supplier
            self.master, text="Delete Supplier", command=self.delete_supplier  # Assigning text and command to the button
        )
        self.delete_button.grid(row=8, column=1, sticky="we")  # Placing button widget in the grid

        self.modify_button = tk.Button(  # Creating button widget for modifying a supplier
            self.master, text="Modify Supplier", command=self.modify_supplier  # Assigning text and command to the button
        )
        self.modify_button.grid(row=9, column=0, sticky="we")  # Placing button widget in the grid

        self.display_button = tk.Button(  # Creating button widget for displaying a supplier
            self.master, text="Display Supplier", command=self.display_supplier  # Assigning text and command to the button
        )
        self.display_button.grid(row=9, column=1, sticky="we")  # Placing button widget in the grid

        self.display_all_button = tk.Button(  # Creating button widget for displaying all suppliers
            self.master, text="Display All Suppliers", command=self.display_all_suppliers  # Assigning text and command to the button
        )
        self.display_all_button.grid(row=10, columnspan=2, column=0, sticky="we")  # Placing button widget in the grid

    def add_supplier(self):  # Method to add a supplier
        supplier_id = self.supplier_id_entry.get()  # Getting supplier ID from entry widget
        name = self.name_entry.get()  # Getting supplier name from entry widget
        address = self.address_entry.get()  # Getting supplier address from entry widget
        contact_details = self.contact_details_entry.get()  # Getting supplier contact details from entry widget
        service_provided = self.service_provided_entry.get()  # Getting service provided by supplier from entry widget
        min_guests_supplier = self.min_guests_supplier_entry.get()  # Getting minimum guests supplied by supplier from entry widget
        max_guests_supplier = self.max_guests_supplier_entry.get()# Getting maximum guests supplied by supplier from entry widget
        menu = self.menu_entry.get()  # Getting menu from entry widget
        try:  # Starting a try block
            new_supplier = Supplier(  # Creating a new Supplier instance
                supplier_id, name, address, contact_details, service_provided, min_guests_supplier, max_guests_supplier, menu)
            self.supplier_management.add_supplier(new_supplier)  # Adding the new supplier
            messagebox.showinfo("Success", "Supplier added successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not add supplier: {e}")  # Displaying error message

    def delete_supplier(self):  # Method to delete a supplier
        supplier_id = self.supplier_id_entry.get()  # Getting supplier ID from entry widget
        try:  # Starting a try block
            self.supplier_management.delete_supplier(supplier_id)  # Deleting the supplier
            messagebox.showinfo("Success", "Supplier deleted successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not delete supplier: {e}")  # Displaying error message

    def modify_supplier(self):  # Method to modify a supplier
        supplier_id = self.supplier_id_entry.get()  # Getting supplier ID from entry widget
        name = self.name_entry.get()  # Getting supplier name from entry widget
        address = self.address_entry.get()  # Getting supplier address from entry widget
        contact_details = self.contact_details_entry.get()  # Getting supplier contact details from entry widget
        service_provided = self.service_provided_entry.get()  # Getting service provided by supplier from entry widget
        min_guests_supplier = self.min_guests_supplier_entry.get()  # Getting minimum guests supplied by supplier from entry widget
        max_guests_supplier = self.max_guests_supplier_entry.get()  # Getting maximum guests supplied by supplier from entry widget
        menu = self.menu_entry.get()  # Getting menu from entry widget
        try:  # Starting a try block
            self.supplier_management.modify_supplier(  # Modifying the supplier
                supplier_id,
                name=name,
                address=address,
                contact_details=contact_details,
                service_provided=service_provided,
                min_guests_supplier=min_guests_supplier,
                max_guests_supplier=max_guests_supplier,
                menu=menu
            )
            messagebox.showinfo("Success", "Supplier modified successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not modify supplier: {e}")  # Displaying error message

    def display_supplier(self):  # Method to display a supplier
        supplier_id = self.supplier_id_entry.get()  # Getting supplier ID from entry widget
        try:  # Starting a try block
            supplier = self.supplier_management.get_supplier(supplier_id)  # Getting the supplier
            supplier_info = f"Supplier ID: {supplier.supplier_id}\nName: {supplier.name}\nAddress: {supplier.address}\nContact Details: {supplier.contact_details}\nService Provided: {supplier.service_provided}"  # Formatting supplier information
            messagebox.showinfo("Supplier Details", supplier_info)  # Displaying supplier information
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not display supplier: {e}")  # Displaying error message

    def display_all_suppliers(self):  # Method to display all suppliers
        try:  # Starting a try block
            all_suppliers_info = self.supplier_management.display_all_suppliers()  # Getting information of all suppliers
            if all_suppliers_info:  # Checking if there are suppliers to display
                messagebox.showinfo("All Suppliers Details", all_suppliers_info)  # Displaying all suppliers information
            else:  # If there are no suppliers to display
                messagebox.showinfo("All Suppliers Details", "No suppliers to display.")  # Displaying message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", str(e))  # Displaying error message


class VenueGUI:
    def __init__(self, master):
        self.master = master  # Initializing the master widget
        self.venue_management = VenueManagement()  # Creating an instance of VenueManagement
        self.create_widgets()  # Calling the method to create GUI widgets

    def create_widgets(self):
        # Venue ID
        tk.Label(self.master, text="Venue ID:").grid(row=0, column=0, sticky="w")  # Creating a label for Venue ID
        self.venue_id_entry = tk.Entry(self.master)  # Creating an entry widget for Venue ID
        self.venue_id_entry.grid(row=0, column=1, sticky="we")  # Placing the entry widget

        # Name
        tk.Label(self.master, text="Name:").grid(row=1, column=0, sticky="w")  # Creating a label for Name
        self.name_entry = tk.Entry(self.master)  # Creating an entry widget for Name
        self.name_entry.grid(row=1, column=1, sticky="we")  # Placing the entry widget

        # Address
        tk.Label(self.master, text="Address:").grid(row=2, column=0, sticky="w")  # Creating a label for Address
        self.address_entry = tk.Entry(self.master)  # Creating an entry widget for Address
        self.address_entry.grid(row=2, column=1, sticky="we")  # Placing the entry widget

        # Contact
        tk.Label(self.master, text="Contact:").grid(row=3, column=0, sticky="w")  # Creating a label for Contact
        self.contact_entry = tk.Entry(self.master)  # Creating an entry widget for Contact
        self.contact_entry.grid(row=3, column=1, sticky="we")  # Placing the entry widget

        # Minimum Guests
        tk.Label(self.master, text="Minimum Guests:").grid(row=4, column=0, sticky="w")  # Creating a label for Minimum Guests
        self.min_guests_entry = tk.Entry(self.master)  # Creating an entry widget for Minimum Guests
        self.min_guests_entry.grid(row=4, column=1, sticky="we")  # Placing the entry widget

        # Maximum Guests
        tk.Label(self.master, text="Maximum Guests:").grid(row=5, column=0, sticky="w")  # Creating a label for Maximum Guests
        self.max_guests_entry = tk.Entry(self.master)  # Creating an entry widget for Maximum Guests
        self.max_guests_entry.grid(row=5, column=1, sticky="we")  # Placing the entry widget

        # Buttons for operations
        self.add_button = tk.Button(
            self.master, text="Add Venue", command=self.add_venue  # Creating a button to add a venue
        )
        self.add_button.grid(row=6, column=0, sticky="we")  # Placing the button widget

        self.delete_button = tk.Button(
            self.master, text="Delete Venue", command=self.delete_venue  # Creating a button to delete a venue
        )
        self.delete_button.grid(row=6, column=1, sticky="we")  # Placing the button widget

        self.modify_button = tk.Button(
            self.master, text="Modify Venue", command=self.modify_venue  # Creating a button to modify a venue
        )
        self.modify_button.grid(row=7, column=0, sticky="we")  # Placing the button widget

        self.display_button = tk.Button(
            self.master, text="Display Venue", command=self.display_venue  # Creating a button to display a venue
        )
        self.display_button.grid(row=7, column=1, sticky="we")  # Placing the button widget

        self.display_all_button = tk.Button(
            self.master, text="Display All Venues", command=self.display_all_venues  # Creating a button to display all venues
        )
        self.display_all_button.grid(row=8, columnspan=2, column=0, sticky="we")  # Placing the button widget

    def add_venue(self):
        venue_id = self.venue_id_entry.get()  # Getting the venue ID from the entry widget
        name = self.name_entry.get()  # Getting the name from the entry widget
        address = self.address_entry.get()  # Getting the address from the entry widget
        contact = self.contact_entry.get()  # Getting the contact from the entry widget
        min_guests = self.min_guests_entry.get()  # Getting the minimum guests from the entry widget
        max_guests = self.max_guests_entry.get()  # Getting the maximum guests from the entry widget
        try:  # Starting a try block
            new_venue = Venue(  # Creating a new Venue object
                venue_id, name, address, contact, int(min_guests), int(max_guests)  # Providing venue details
            )
            self.venue_management.add_venue(new_venue)  # Adding the new venue
            messagebox.showinfo("Success", "Venue added successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not add venue: {e}")  # Displaying error message

    def delete_venue(self):
        venue_id = self.venue_id_entry.get()  # Getting the venue ID from the entry widget
        try:  # Starting a try block
            self.venue_management.delete_venue(venue_id)  # Deleting the venue
            messagebox.showinfo("Success", "Venue deleted successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not delete venue: {e}")  # Displaying error message

    def modify_venue(self):
        venue_id = self.venue_id_entry.get()  # Getting the venue ID from the entry widget
        name = self.name_entry.get()  # Getting the name from the entry widget
        address = self.address_entry.get()  # Getting the address from the entry widget
        contact = self.contact_entry.get()  # Getting the contact from the entry widget
        min_guests = self.min_guests_entry.get()  # Getting the minimum guests from the entry widget
        max_guests = self.max_guests_entry.get()  # Getting the maximum guests from the entry widget
        try:  # Starting a try block
            self.venue_management.modify_venue(  # Modifying the venue
                venue_id,
                name=name,
                address=address,
                contact=contact,
                min_guests=int(min_guests),
                max_guests=int(max_guests),
            )
            messagebox.showinfo("Success", "Venue modified successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not modify venue: {e}")  # Displaying error message

    def display_all_venues(self):  # Method to display all venues
        try:  # Starting a try block
            all_venues_info = self.venue_management.display_all_venues()  # Retrieving all venue information
            if all_venues_info:  # Checking if there are venues to display
                messagebox.showinfo("All Venues Details", all_venues_info)  # Displaying all venue details
            else:  # If there are no venues
                messagebox.showinfo("All Venues Details", "No venues to display.")  # Displaying message indicating no venues
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", str(e))  # Displaying error message

    def display_venue(self):  # Method to display a venue
        venue_id = self.venue_id_entry.get()  # Getting venue ID from entry widget
        try:  # Starting a try block
            venue = self.venue_management.get_venue(venue_id)  # Retrieving the venue
            venue_info = f"Venue ID: {venue.venue_id}\nName: {venue.name}\nAddress: {venue.address}\nContact: {venue.contact}\nMinimum Guests: {venue.min_guests}\nMaximum Guests: {venue.max_guests}"
            messagebox.showinfo("Venue Details", venue_info)  # Displaying venue details
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not display venue: {e}")  # Displaying error message


class ClientGUI:
    def __init__(self, master):
        self.master = master  # Initializing the master widget
        self.client_management = ClientManagement()  # Creating an instance of ClientManagement
        self.create_widgets()  # Calling the method to create GUI widgets

    def create_widgets(self):
        # Client ID
        tk.Label(self.master, text="Client ID:").grid(row=0, column=0, sticky="w")  # Creating a label for Client ID
        self.client_id_entry = tk.Entry(self.master)  # Creating an entry widget for Client ID
        self.client_id_entry.grid(row=0, column=1, sticky="we")  # Placing the entry widget

        # Name
        tk.Label(self.master, text="Name:").grid(row=1, column=0, sticky="w")  # Creating a label for Name
        self.name_entry = tk.Entry(self.master)  # Creating an entry widget for Name
        self.name_entry.grid(row=1, column=1, sticky="we")  # Placing the entry widget

        # Address
        tk.Label(self.master, text="Address:").grid(row=2, column=0, sticky="w")  # Creating a label for Address
        self.address_entry = tk.Entry(self.master)  # Creating an entry widget for Address
        self.address_entry.grid(row=2, column=1, sticky="we")  # Placing the entry widget

        # Contact Details
        tk.Label(self.master, text="Contact Details:").grid(row=3, column=0, sticky="w")  # Creating a label for Contact Details
        self.contact_details_entry = tk.Entry(self.master)  # Creating an entry widget for Contact Details
        self.contact_details_entry.grid(row=3, column=1, sticky="we")  # Placing the entry widget

        # Budget
        tk.Label(self.master, text="Budget:").grid(row=4, column=0, sticky="w")  # Creating a label for Budget
        self.budget_entry = tk.Entry(self.master)  # Creating an entry widget for Budget
        self.budget_entry.grid(row=4, column=1, sticky="we")  # Placing the entry widget

        # Buttons
        self.add_button = tk.Button(
            self.master, text="Add Client", command=self.add_client  # Creating a button to add a client
        )
        self.add_button.grid(row=5, column=0, sticky="we")  # Placing the button widget

        self.delete_button = tk.Button(
            self.master, text="Delete Client", command=self.delete_client  # Creating a button to delete a client
        )
        self.delete_button.grid(row=5, column=1, sticky="we")  # Placing the button widget

        self.modify_button = tk.Button(
            self.master, text="Modify Client", command=self.modify_client  # Creating a button to modify a client
        )
        self.modify_button.grid(row=6, column=0, sticky="we")  # Placing the button widget

        self.display_button = tk.Button(
            self.master, text="Display Client", command=self.display_client  # Creating a button to display a client
        )
        self.display_button.grid(row=6, column=1, sticky="we")  # Placing the button widget

        self.display_all_button = tk.Button(
            self.master, text="Display All Clients", command=self.display_all_clients  # Creating a button to display all clients
        )
        self.display_all_button.grid(row=7, columnspan=2, column=0, sticky="we")  # Placing the button widget

    def add_client(self):
        client_id = self.client_id_entry.get()  # Getting the client ID from the entry widget
        name = self.name_entry.get()  # Getting the name from the entry widget
        address = self.address_entry.get()  # Getting the address from the entry widget
        contact_details = self.contact_details_entry.get()  # Getting the contact details from the entry widget
        budget = self.budget_entry.get()  # Getting the budget from the entry widget
        try:  # Starting a try block
            budget = float(budget)  # Converting budget to float
            client = Client(client_id, name, address, contact_details, budget)  # Creating a new Client object
            self.client_management.add_client(client)  # Adding the new client
            messagebox.showinfo("Success", "Client added successfully.")  # Displaying success message
        except ValueError as e:  # Catching value error
            messagebox.showerror("Error", f"Invalid input: {e}")  # Displaying error message for invalid input
        except Exception as e:  # Catching other exceptions
            messagebox.showerror("Error", str(e))  # Displaying error message

    def delete_client(self):
        client_id = self.client_id_entry.get()  # Getting the client ID from the entry widget
        try:  # Starting a try block
            self.client_management.delete_client(client_id)  # Deleting the client
            messagebox.showinfo("Success", "Client deleted successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", str(e))  # Displaying error message

    def modify_client(self):
        client_id = self.client_id_entry.get()  # Getting the client ID from the entry widget
        name = self.name_entry.get()  # Getting the name from the entry widget
        address = self.address_entry.get()  # Getting the address from the entry widget
        contact_details = self.contact_details_entry.get()  # Getting the contact details from the entry widget
        budget = self.budget_entry.get()  # Getting the budget from the entry widget
        try:  # Starting a try block
            budget = float(budget)  # Converting budget to float
            self.client_management.modify_client(  # Modifying the client
                client_id,
                name=name,
                address=address,
                contact_details=contact_details,
                budget=budget,
            )
            messagebox.showinfo("Success", "Client modified successfully.")  # Displaying success message
        except ValueError as e:  # Catching value error
            messagebox.showerror("Error", f"Invalid input: {e}")  # Displaying error message for invalid input
        except Exception as e:  # Catching other exceptions
            messagebox.showerror("Error", str(e))  # Displaying error message

    def display_client(self):
        client_id = self.client_id_entry.get()  # Getting the client ID from the entry widget
        try:  # Starting a try block
            client = self.client_management.get_client(client_id)  # Retrieving the client
            info = f"Client ID: {client.client_id}\nName: {client.name}\nAddress: {client.address}\nContact Details: {client.contact_details}\nBudget: {client.budget}"
            messagebox.showinfo("Client Details", info)  # Displaying client details
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", str(e))  # Displaying error message

    def display_all_clients(self):
        try:  # Starting a try block
            all_clients_info = self.client_management.display_all_clients()  # Retrieving all clients' information
            if all_clients_info:  # Checking if there are clients to display
                messagebox.showinfo("All Clients Details", all_clients_info)  # Displaying all client details
            else:  # If there are no clients
                messagebox.showinfo("All Clients Details", "No clients to display.")  # Displaying message indicating no clients
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", str(e))  # Displaying error message

class EmployeeGUI:
    def __init__(self, master):
        self.master = master  # Initializing the master widget
        self.employee_management = EmployeeManagement()  # Creating an instance of EmployeeManagement
        self.create_widgets()  # Calling the method to create GUI widgets

    def create_widgets(self):
        # Employee ID
        tk.Label(self.master, text="Employee ID:").grid(row=0, column=0, sticky="w")  # Creating a label for Employee ID
        self.employee_id_entry = tk.Entry(self.master)  # Creating an entry widget for Employee ID
        self.employee_id_entry.grid(row=0, column=1, sticky="we")  # Placing the entry widget

        # Name
        tk.Label(self.master, text="Name:").grid(row=1, column=0, sticky="w")  # Creating a label for Name
        self.name_entry = tk.Entry(self.master)  # Creating an entry widget for Name
        self.name_entry.grid(row=1, column=1, sticky="we")  # Placing the entry widget

        # Department
        tk.Label(self.master, text="Department:").grid(row=2, column=0, sticky="w")  # Creating a label for Department
        self.department_entry = tk.Entry(self.master)  # Creating an entry widget for Department
        self.department_entry.grid(row=2, column=1, sticky="we")  # Placing the entry widget

        # Job Title
        tk.Label(self.master, text="Job Title:").grid(row=3, column=0, sticky="w")  # Creating a label for Job Title
        self.job_title_entry = tk.Entry(self.master)  # Creating an entry widget for Job Title
        self.job_title_entry.grid(row=3, column=1, sticky="we")  # Placing the entry widget

        # Basic Salary
        tk.Label(self.master, text="Basic Salary:").grid(row=4, column=0, sticky="w")  # Creating a label for Basic Salary
        self.basic_salary_entry = tk.Entry(self.master)  # Creating an entry widget for Basic Salary
        self.basic_salary_entry.grid(row=4, column=1, sticky="we")  # Placing the entry widget

        tk.Label(self.master, text="Age:").grid(row=5, column=0, sticky="w")  # Creating a label for Age
        self.age_entry = tk.Entry(self.master)  # Creating an entry widget for Age
        self.age_entry.grid(row=5, column=1, sticky="we")  # Placing the entry widget

        # Date of Birth
        tk.Label(self.master, text="Date of Birth:").grid(row=6, column=0, sticky="w")  # Creating a label for Date of Birth
        self.dob_entry = tk.Entry(self.master)  # Creating an entry widget for Date of Birth
        self.dob_entry.grid(row=6, column=1, sticky="we")  # Placing the entry widget

        # Passport Details
        tk.Label(self.master, text="Passport Details:").grid(
            row=7, column=0, sticky="w"  # Creating a label for Passport Details
        )
        self.passport_entry = tk.Entry(self.master)  # Creating an entry widget for Passport Details
        self.passport_entry.grid(row=7, column=1, sticky="we")  # Placing the entry widget

        # Manager ID
        tk.Label(self.master, text="Manager ID:").grid(row=8, column=0, sticky="w")  # Creating a label for Manager ID
        self.manager_id_entry = tk.Entry(self.master)  # Creating an entry widget for Manager ID
        self.manager_id_entry.grid(row=8, column=1, sticky="we")  # Placing the entry widget

        # Buttons for operations
        self.add_button = tk.Button(
            self.master, text="Add Employee", command=self.add_employee  # Creating a button to add an employee
        )
        self.add_button.grid(row=9, column=0, sticky="we")  # Placing the button widget

        self.delete_button = tk.Button(
            self.master, text="Delete Employee", command=self.delete_employee  # Creating a button to delete an employee
        )
        self.delete_button.grid(row=9, column=1, sticky="we")  # Placing the button widget

        self.modify_button = tk.Button(self.master, text="Modify Employee", command=self.modify_employee)
        self.modify_button.grid(row=10, column=0, sticky="we")  # Creating a button to modify an employee

        self.display_button = tk.Button(
            self.master, text="Display Employee", command=self.display_employee  # Creating a button to display an employee
        )
        self.display_button.grid(row=10, column=1, sticky="we")  # Placing the button widget

        self.display_all_button = tk.Button(self.master, text="Display All Employee", command=self.display_all_employees)
        self.display_all_button.grid(row=11, columnspan=2, column=0, sticky="we")  # Placing the button widget

    def add_employee(self):
        try:  # Starting a try block
            new_employee = Employee(  # Creating a new Employee object
                name=self.name_entry.get(),
                employee_id=self.employee_id_entry.get(),
                department=self.department_entry.get(),
                job_title=self.job_title_entry.get(),
                basic_salary=self.basic_salary_entry.get(),
                age=self.age_entry.get(),
                date_of_birth=self.dob_entry.get(),
                passport_details=self.passport_entry.get(),
                manager_id=self.manager_id_entry.get() or None,
            )
            self.employee_management.add_employee(new_employee)  # Adding the new employee
            messagebox.showinfo("Success", "Employee added successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not add employee: {e}")  # Displaying error message

    def delete_employee(self):
        employee_id = self.employee_id_entry.get()  # Getting the employee ID from the entry widget
        try:  # Starting a try block
            self.employee_management.delete_employee(employee_id)  # Deleting the employee
            messagebox.showinfo("Success", "Employee deleted successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not delete employee: {e}")  # Displaying error message

    def modify_employee(self):
        employee_id = self.employee_id_entry.get()  # Getting the employee ID from the entry widget
        try:  # Starting a try block
            self.employee_management.modify_employee(  # Modifying the employee
                employee_id,
                name=self.name_entry.get(),
                department=self.department_entry.get(),
                job_title=self.job_title_entry.get(),
                basic_salary=self.basic_salary_entry.get(),
                age=self.age_entry.get(),
                date_of_birth=self.dob_entry.get(),
                passport_details=self.passport_entry.get(),
                manager_id=self.manager_id_entry.get() or None,
            )
            messagebox.showinfo("Success", "Employee modified successfully.")  # Displaying success message
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not modify employee: {e}")  # Displaying error message

    def display_employee(self):
        employee_id = self.employee_id_entry.get()  # Getting the employee ID from the entry widget
        try:  # Starting a try block
            employee = self.employee_management.get_employee(employee_id)  # Retrieving the employee
            employee_info = (  # Constructing employee information
                f"Name: {employee.name}\n"
                f"Department: {employee.department}\n"
                f"Job Title: {employee.job_title}\n"
                f"Basic Salary: {employee.basic_salary}\n"
                f"Age: {employee.age}\n"
                f"Date of Birth: {employee.date_of_birth}\n"
                f"Passport Details: {employee.passport_details}\n"
                f"Manager ID: {employee.manager_id}"
            )
            messagebox.showinfo("Employee Details", employee_info)  # Displaying employee information
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", f"Could not display employee: {e}")  # Displaying error message

    def display_all_employees(self):
        try:  # Starting a try block
            all_employees_info = self.employee_management.display_all_employees()  # Retrieving all employees' information
            if all_employees_info:  # Checking if there are employees to display
                messagebox.showinfo("All Employees Details", all_employees_info)  # Displaying all employees' details
            else:  # If there are no employees
                messagebox.showinfo("All Employees Details", "No employees to display.")  # Displaying message indicating no employees
        except Exception as e:  # Catching any exceptions
            messagebox.showerror("Error", str(e))  # Displaying error message

class ManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()  # Calling the constructor of the superclass
        self.title("Events Company Management System")  # Setting the title of the application window
        self.geometry("500x400")  # Setting the size of the application window

        self.tab_control = ttk.Notebook(self)  # Creating a tab control
        self.init_tabs()  # Initializing tabs
        self.tab_control.pack(expand=1, fill="both")  # Packing the tab control

    def init_tabs(self):
        # Client Tab
        self.client_tab = ttk.Frame(self.tab_control)  # Creating a frame for the client tab
        self.client_gui = ClientGUI(self.client_tab)  # Creating an instance of ClientGUI
        self.client_tab.pack(fill="both", expand=True)  # Packing the client tab frame
        self.tab_control.add(self.client_tab, text="Clients")  # Adding the client tab to the tab control

        # Employee Tab
        self.employee_tab = ttk.Frame(self.tab_control)  # Creating a frame for the employee tab
        self.employee_gui = EmployeeGUI(self.employee_tab)  # Creating an instance of EmployeeGUI
        self.employee_tab.pack(fill="both", expand=True)  # Packing the employee tab frame
        self.tab_control.add(self.employee_tab, text="Employees")  # Adding the employee tab to the tab control

        # Event Tab
        self.event_tab = ttk.Frame(self.tab_control)  # Creating a frame for the event tab
        self.event_gui = EventGUI(self.event_tab)  # Creating an instance of EventGUI
        self.event_tab.pack(fill="both", expand=True)  # Packing the event tab frame
        self.tab_control.add(self.event_tab, text="Events")  # Adding the event tab to the tab control

        # Guest Tab
        self.guest_tab = ttk.Frame(self.tab_control)  # Creating a frame for the guest tab
        self.guest_gui = GuestGUI(self.guest_tab)  # Creating an instance of GuestGUI
        self.guest_tab.pack(fill="both", expand=True)  # Packing the guest tab frame
        self.tab_control.add(self.guest_tab, text="Guests")  # Adding the guest tab to the tab control

        # Supplier Tab
        self.supplier_tab = ttk.Frame(self.tab_control)  # Creating a frame for the supplier tab
        self.supplier_gui = SupplierGUI(self.supplier_tab)  # Creating an instance of SupplierGUI
        self.supplier_tab.pack(fill="both", expand=True)  # Packing the supplier tab frame
        self.tab_control.add(self.supplier_tab, text="Suppliers")  # Adding the supplier tab to the tab control

        # Venue Tab
        self.venue_tab = ttk.Frame(self.tab_control)  # Creating a frame for the venue tab
        self.venue_gui = VenueGUI(self.venue_tab)  # Creating an instance of VenueGUI
        self.venue_tab.pack(fill="both", expand=True)  # Packing the venue tab frame
        self.tab_control.add(self.venue_tab, text="Venues")  # Adding the venue tab to the tab control


if __name__ == "__main__":
    app = ManagementApp()  # Creating an instance of ManagementApp
    app.mainloop()  # Running the main event loop

