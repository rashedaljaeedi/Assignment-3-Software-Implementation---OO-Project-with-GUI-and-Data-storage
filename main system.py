import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from event_management import Event, EventManagement
from guest_management import Guest, GuestManagement
from supplier_management import Supplier, SupplierManagement
from venue_management import Venue, VenueManagement
from client_management import Client, ClientManagement
from employee_management import Employee, EmployeeManagement


class EventGUI:
    def __init__(self, master):
        self.master = master
        self.event_management = EventManagement()
        self.create_widgets()

    def create_widgets(self):

        # Widgets for event management GUI
        labels = [
            "Event ID:",
            "Type:",
            "Theme:",
            "Date:",
            "Time:",
            "Duration:",
            "Venue Address:",
            "Client ID:",
            "Catering Company:",
            "Cleaning Company:",
            "Decorations Company:",
            "Guest List",
            "Entertainment Company",
            "Furniture Company",
            "Invoice",

        ]
        self.entries = {}
        for i, label in enumerate(labels):
            tk.Label(self.master, text=label).grid(row=i, column=0, sticky="w")
            entry = tk.Entry(self.master)
            entry.grid(row=i, column=1, sticky="we")
            self.entries[label.strip(":")] = entry

        operations = [
            ("Add Event", self.add_event),
            ("Delete Event", self.delete_event),
            ("Modify Event", self.modify_event),
            ("Display Event", self.display_event),
            ("Display All Events", self.display_all_events)
        ]
        for i, (text, command) in enumerate(operations, start=len(labels)):
            button = tk.Button(self.master, text=text, command=command)
            button.grid(row=i, columnspan=2, sticky="we")



    def add_event(self):
        try:
            event_data = {key: entry.get() for key, entry in self.entries.items()}

            event_data["event_id"] = event_data.pop("Event ID")
            event_data["event_type"] = event_data.pop("Type")
            event_data["theme"] = event_data.pop("Theme")
            event_data["date"] = event_data.pop("Date")
            event_data["time"] = event_data.pop("Time")
            event_data["duration"] = event_data.pop("Duration")
            event_data["venue_address"] = event_data.pop("Venue Address")
            event_data["client_id"] = event_data.pop("Client ID")
            event_data["catering_company"] = event_data.pop("Catering Company")
            event_data["cleaning_company"] = event_data.pop("Cleaning Company")
            event_data["decorations_company"] = event_data.pop("Decorations Company")
            event_data["guest_list"] = event_data.pop("Guest List")
            event_data["entertainment_company"] = event_data.pop("Entertainment Company")
            event_data["furniture_supply_company"] = event_data.pop("Furniture Company")
            event_data["invoice"] = event_data.pop("Invoice")


            new_event = Event(**event_data)
            self.event_management.add_event(new_event)
            messagebox.showinfo("Success", "Event added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not add event: {e}")

    def delete_event(self):
        event_id = self.entries["Event ID"].get()
        try:
            self.event_management.delete_event(event_id)
            messagebox.showinfo("Success", "Event deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete event: {e}")

    def modify_event(self):
        event_id = self.entries["Event ID"].get()
        updates = {
            key: entry.get() for key, entry in self.entries.items() if entry.get()
        }
        try:
            self.event_management.modify_event(event_id, **updates)
            messagebox.showinfo("Success", "Event modified successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not modify event: {e}")

    def display_event(self):
        event_id = self.entries["Event ID"].get()
        try:
            event = self.event_management.get_event(event_id)
            event_info = "\n".join(
                f"{key}: {getattr(event, key.lower().replace(' ', '_'), '')}"
                for key in self.entries
            )
            messagebox.showinfo("Event Details", event_info)
        except Exception as e:
            messagebox.showerror("Error", f"Could not display event: {e}")

    def display_all_events(self):
        try:
            all_events_info = self.event_management.display_all_events()
            if all_events_info:
                messagebox.showinfo("All Events Details", all_events_info)
            else:
                messagebox.showinfo("All Events Details", "No events to display.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


class GuestGUI:
    def __init__(self, master):
        self.master = master
        self.guest_management = GuestManagement()
        self.create_widgets()

    def create_widgets(self):
        # Guest ID
        tk.Label(self.master, text="Guest ID:").grid(row=0, column=0, sticky="w")
        self.guest_id_entry = tk.Entry(self.master)
        self.guest_id_entry.grid(row=0, column=1, sticky="we")

        # Name
        tk.Label(self.master, text="Name:").grid(row=1, column=0, sticky="w")
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=1, column=1, sticky="we")

        # Address
        tk.Label(self.master, text="Address:").grid(row=2, column=0, sticky="w")
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=2, column=1, sticky="we")

        # Contact Details
        tk.Label(self.master, text="Contact Details:").grid(row=3, column=0, sticky="w")
        self.contact_details_entry = tk.Entry(self.master)
        self.contact_details_entry.grid(row=3, column=1, sticky="we")

        # Buttons for operations
        self.add_button = tk.Button(
            self.master, text="Add Guest", command=self.add_guest
        )
        self.add_button.grid(row=4, column=0, sticky="we")

        self.delete_button = tk.Button(
            self.master, text="Delete Guest", command=self.delete_guest
        )
        self.delete_button.grid(row=4, column=1, sticky="we")

        self.modify_button = tk.Button(
            self.master, text="Modify Guest", command=self.modify_guest
        )
        self.modify_button.grid(row=5, column=0, sticky="we")

        self.display_button = tk.Button(
            self.master, text="Display Guest", command=self.display_guest
        )
        self.display_button.grid(row=5, column=1, sticky="we")

        self.display_all_button = tk.Button(
            self.master, text="Display All Guests", command=self.display_all_guests
        )
        self.display_all_button.grid(row=6, column=0,columnspan=2, sticky="we")

    def add_guest(self):
        guest_id = self.guest_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        try:
            new_guest = Guest(guest_id, name, address, contact_details)
            self.guest_management.add_guest(new_guest)
            messagebox.showinfo("Success", "Guest added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not add guest: {e}")

    def delete_guest(self):
        guest_id = self.guest_id_entry.get()
        try:
            self.guest_management.delete_guest(guest_id)
            messagebox.showinfo("Success", "Guest deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete guest: {e}")

    def modify_guest(self):
        guest_id = self.guest_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        try:
            self.guest_management.modify_guest(
                guest_id, name=name, address=address, contact_details=contact_details
            )
            messagebox.showinfo("Success", "Guest modified successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not modify guest: {e}")

    def display_guest(self):
        guest_id = self.guest_id_entry.get()
        try:
            guest = self.guest_management.get_guest(guest_id)
            guest_info = f"Guest ID: {guest.guest_id}\nName: {guest.name}\nAddress: {guest.address}\nContact Details: {guest.contact_details}"
            messagebox.showinfo("Guest Details", guest_info)
        except Exception as e:
            messagebox.showerror("Error", f"Could not display guest: {e}")

    def display_all_guests(self):
        try:
            all_guests_info = self.guest_management.display_all_guests()
            if all_guests_info:
                messagebox.showinfo("All Guests Details", all_guests_info)
            else:
                messagebox.showinfo("All Guests Details", "No guests to display.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


class SupplierGUI:
    def __init__(self, master):
        self.master = master
        self.supplier_management = SupplierManagement()
        self.create_widgets()

    def create_widgets(self):
        # Supplier ID
        tk.Label(self.master, text="Supplier ID:").grid(row=0, column=0, sticky="w")
        self.supplier_id_entry = tk.Entry(self.master)
        self.supplier_id_entry.grid(row=0, column=1, sticky="we")

        # Name
        tk.Label(self.master, text="Name:").grid(row=1, column=0, sticky="w")
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=1, column=1, sticky="we")

        # Address
        tk.Label(self.master, text="Address:").grid(row=2, column=0, sticky="w")
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=2, column=1, sticky="we")

        # Contact Details
        tk.Label(self.master, text="Contact Details:").grid(row=3, column=0, sticky="w")
        self.contact_details_entry = tk.Entry(self.master)
        self.contact_details_entry.grid(row=3, column=1, sticky="we")

        # Service Provided
        tk.Label(self.master, text="Service Provided:").grid(
            row=4, column=0, sticky="w"
        )
        self.service_provided_entry = tk.Entry(self.master)
        self.service_provided_entry.grid(row=4, column=1, sticky="we")

        # Buttons for operations
        self.add_button = tk.Button(
            self.master, text="Add Supplier", command=self.add_supplier
        )
        self.add_button.grid(row=5, column=0, sticky="we")

        self.delete_button = tk.Button(
            self.master, text="Delete Supplier", command=self.delete_supplier
        )
        self.delete_button.grid(row=5, column=1, sticky="we")

        self.modify_button = tk.Button(
            self.master, text="Modify Supplier", command=self.modify_supplier
        )
        self.modify_button.grid(row=6, column=0, sticky="we")

        self.display_button = tk.Button(
            self.master, text="Display Supplier", command=self.display_supplier
        )
        self.display_button.grid(row=6, column=1, sticky="we")

        self.display_all_button = tk.Button(
            self.master, text="Display All Suppliers", command=self.display_all_suppliers
        )
        self.display_all_button.grid(row=7 ,columnspan=2,column=0, sticky="we")
    def add_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        service_provided = self.service_provided_entry.get()
        try:
            new_supplier = Supplier(
                supplier_id, name, address, contact_details, service_provided
            )
            self.supplier_management.add_supplier(new_supplier)
            messagebox.showinfo("Success", "Supplier added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not add supplier: {e}")

    def delete_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        try:
            self.supplier_management.delete_supplier(supplier_id)
            messagebox.showinfo("Success", "Supplier deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete supplier: {e}")

    def modify_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        service_provided = self.service_provided_entry.get()
        try:
            self.supplier_management.modify_supplier(
                supplier_id,
                name=name,
                address=address,
                contact_details=contact_details,
                service_provided=service_provided,
            )
            messagebox.showinfo("Success", "Supplier modified successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not modify supplier: {e}")

    def display_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        try:
            supplier = self.supplier_management.get_supplier(supplier_id)
            supplier_info = f"Supplier ID: {supplier.supplier_id}\nName: {supplier.name}\nAddress: {supplier.address}\nContact Details: {supplier.contact_details}\nService Provided: {supplier.service_provided}"
            messagebox.showinfo("Supplier Details", supplier_info)
        except Exception as e:
            messagebox.showerror("Error", f"Could not display supplier: {e}")

    def display_all_suppliers(self):
        try:
            all_suppliers_info = self.supplier_management.display_all_suppliers()
            if all_suppliers_info:
                messagebox.showinfo("All Suppliers Details", all_suppliers_info)
            else:
                messagebox.showinfo("All Suppliers Details", "No suppliers to display.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


class VenueGUI:
    def __init__(self, master):
        self.master = master
        self.venue_management = VenueManagement()
        self.create_widgets()

    def create_widgets(self):
        # Venue ID
        tk.Label(self.master, text="Venue ID:").grid(row=0, column=0, sticky="w")
        self.venue_id_entry = tk.Entry(self.master)
        self.venue_id_entry.grid(row=0, column=1, sticky="we")

        # Name
        tk.Label(self.master, text="Name:").grid(row=1, column=0, sticky="w")
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=1, column=1, sticky="we")

        # Address
        tk.Label(self.master, text="Address:").grid(row=2, column=0, sticky="w")
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=2, column=1, sticky="we")

        # Contact
        tk.Label(self.master, text="Contact:").grid(row=3, column=0, sticky="w")
        self.contact_entry = tk.Entry(self.master)
        self.contact_entry.grid(row=3, column=1, sticky="we")

        # Minimum Guests
        tk.Label(self.master, text="Minimum Guests:").grid(row=4, column=0, sticky="w")
        self.min_guests_entry = tk.Entry(self.master)
        self.min_guests_entry.grid(row=4, column=1, sticky="we")

        # Maximum Guests
        tk.Label(self.master, text="Maximum Guests:").grid(row=5, column=0, sticky="w")
        self.max_guests_entry = tk.Entry(self.master)
        self.max_guests_entry.grid(row=5, column=1, sticky="we")

        # Buttons for operations
        self.add_button = tk.Button(
            self.master, text="Add Venue", command=self.add_venue
        )
        self.add_button.grid(row=6, column=0, sticky="we")

        self.delete_button = tk.Button(
            self.master, text="Delete Venue", command=self.delete_venue
        )
        self.delete_button.grid(row=6, column=1, sticky="we")

        self.modify_button = tk.Button(
            self.master, text="Modify Venue", command=self.modify_venue
        )
        self.modify_button.grid(row=7, column=0, sticky="we")

        self.display_button = tk.Button(
            self.master, text="Display Venue", command=self.display_venue
        )
        self.display_button.grid(row=7, column=1, sticky="we")

        self.display_all_button = tk.Button(
            self.master, text="Display All Venues", command=self.display_all_venues
        )
        self.display_all_button.grid(row=8, columnspan=2, column=0, sticky="we")

    def add_venue(self):
        venue_id = self.venue_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact = self.contact_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()
        try:
            new_venue = Venue(
                venue_id, name, address, contact, int(min_guests), int(max_guests)
            )
            self.venue_management.add_venue(new_venue)
            messagebox.showinfo("Success", "Venue added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not add venue: {e}")

    def delete_venue(self):
        venue_id = self.venue_id_entry.get()
        try:
            self.venue_management.delete_venue(venue_id)
            messagebox.showinfo("Success", "Venue deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete venue: {e}")

    def modify_venue(self):
        venue_id = self.venue_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact = self.contact_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()
        try:
            self.venue_management.modify_venue(
                venue_id,
                name=name,
                address=address,
                contact=contact,
                min_guests=int(min_guests),
                max_guests=int(max_guests),
            )
            messagebox.showinfo("Success", "Venue modified successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not modify venue: {e}")


    def display_all_venues(self):
        try:
            all_venues_info = self.venue_management.display_all_venues()
            if all_venues_info:
                messagebox.showinfo("All Venues Details", all_venues_info)
            else:
                messagebox.showinfo("All Venues Details", "No venues to display.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_venue(self):
        venue_id = self.venue_id_entry.get()
        try:
            venue = self.venue_management.get_venue(venue_id)
            venue_info = f"Venue ID: {venue.venue_id}\nName: {venue.name}\nAddress: {venue.address}\nContact: {venue.contact}\nMinimum Guests: {venue.min_guests}\nMaximum Guests: {venue.max_guests}"
            messagebox.showinfo("Venue Details", venue_info)
        except Exception as e:
            messagebox.showerror("Error", f"Could not display venue: {e}")


class ClientGUI:
    def __init__(self, master):
        self.master = master
        self.client_management = ClientManagement()
        self.create_widgets()

    def create_widgets(self):



        # Client ID
        tk.Label(self.master, text="Client ID:").grid(row=0, column=0, sticky="w")
        self.client_id_entry = tk.Entry(self.master)
        self.client_id_entry.grid(row=0, column=1, sticky="we")

        # Name
        tk.Label(self.master, text="Name:").grid(row=1, column=0, sticky="w")
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=1, column=1, sticky="we")

        # Address
        tk.Label(self.master, text="Address:").grid(row=2, column=0, sticky="w")
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=2, column=1, sticky="we")

        # Contact Details
        tk.Label(self.master, text="Contact Details:").grid(row=3, column=0, sticky="w")
        self.contact_details_entry = tk.Entry(self.master)
        self.contact_details_entry.grid(row=3, column=1, sticky="we")

        # Budget
        tk.Label(self.master, text="Budget:").grid(row=4, column=0, sticky="w")
        self.budget_entry = tk.Entry(self.master)
        self.budget_entry.grid(row=4, column=1, sticky="we")



        # Buttons
        self.add_button = tk.Button(
            self.master, text="Add Client", command=self.add_client )
        self.add_button.grid(row=5, column=0, sticky="we")

        self.delete_button = tk.Button(
            self.master, text="Delete Client", command=self.delete_client
        )
        self.delete_button.grid(row=5, column=1, sticky="we")

        self.modify_button = tk.Button(
            self.master, text="Modify Client", command=self.modify_client
        )
        self.modify_button.grid(row=6, column=0, sticky="we")

        self.display_button = tk.Button(
            self.master, text="Display Client", command=self.display_client
        )
        self.display_button.grid(row=6, column=1, sticky="we")

        self.display_all_button = tk.Button(self.master, text="Display All Clients", command=self.display_all_clients)
        self.display_all_button.grid(row=7, columnspan=2, column=0, sticky="we")



    def add_client(self):
        client_id = self.client_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        budget = self.budget_entry.get()
        try:
            budget = float(budget)
            client = Client(client_id, name, address, contact_details, budget)
            self.client_management.add_client(client)
            messagebox.showinfo("Success", "Client added successfully.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_client(self):
        client_id = self.client_id_entry.get()
        try:
            self.client_management.delete_client(client_id)
            messagebox.showinfo("Success", "Client deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def modify_client(self):
        client_id = self.client_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        budget = self.budget_entry.get()
        try:
            budget = float(budget)
            self.client_management.modify_client(
                client_id,
                name=name,
                address=address,
                contact_details=contact_details,
                budget=budget,
            )
            messagebox.showinfo("Success", "Client modified successfully.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_client(self):
        client_id = self.client_id_entry.get()
        try:
            client = self.client_management.get_client(client_id)
            info = f"Client ID: {client.client_id}\nName: {client.name}\nAddress: {client.address}\nContact Details: {client.contact_details}\nBudget: {client.budget}"
            messagebox.showinfo("Client Details", info)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_all_clients(self):
        try:
            all_clients_info = self.client_management.display_all_clients()
            if all_clients_info:
                messagebox.showinfo("All Clients Details", all_clients_info)
            else:
                messagebox.showinfo("All Clients Details", "No clients to display.")
        except Exception as e:
            messagebox.showerror("Error", str(e))




class EmployeeGUI:
    def __init__(self, master):
        self.master = master
        self.employee_management = EmployeeManagement()
        self.create_widgets()

    def create_widgets(self):
        # Employee ID
        tk.Label(self.master, text="Employee ID:").grid(row=0, column=0, sticky="w")
        self.employee_id_entry = tk.Entry(self.master)
        self.employee_id_entry.grid(row=0, column=1, sticky="we")

        # Name
        tk.Label(self.master, text="Name:").grid(row=1, column=0, sticky="w")
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=1, column=1, sticky="we")

        # Department
        tk.Label(self.master, text="Department:").grid(row=2, column=0, sticky="w")
        self.department_entry = tk.Entry(self.master)
        self.department_entry.grid(row=2, column=1, sticky="we")

        # Job Title
        tk.Label(self.master, text="Job Title:").grid(row=3, column=0, sticky="w")
        self.job_title_entry = tk.Entry(self.master)
        self.job_title_entry.grid(row=3, column=1, sticky="we")

        # Basic Salary
        tk.Label(self.master, text="Basic Salary:").grid(row=4, column=0, sticky="w")
        self.basic_salary_entry = tk.Entry(self.master)
        self.basic_salary_entry.grid(row=4, column=1, sticky="we")

        tk.Label(self.master, text="Age:").grid(row=5, column=0, sticky="w")
        self.age_entry = tk.Entry(self.master)
        self.age_entry.grid(row=5, column=1, sticky="we")

        # Date of Birth
        tk.Label(self.master, text="Date of Birth:").grid(row=6, column=0, sticky="w")
        self.dob_entry = tk.Entry(self.master)
        self.dob_entry.grid(row=6, column=1, sticky="we")

        # Passport Details
        tk.Label(self.master, text="Passport Details:").grid(
            row=7, column=0, sticky="w"
        )
        self.passport_entry = tk.Entry(self.master)
        self.passport_entry.grid(row=7, column=1, sticky="we")

        # Manager ID
        tk.Label(self.master, text="Manager ID:").grid(row=8, column=0, sticky="w")
        self.manager_id_entry = tk.Entry(self.master)
        self.manager_id_entry.grid(row=8, column=1, sticky="we")

        # Buttons for operations
        self.add_button = tk.Button(
            self.master, text="Add Employee", command=self.add_employee
        )
        self.add_button.grid(row=9, column=0, sticky="we")

        self.delete_button = tk.Button(
            self.master, text="Delete Employee", command=self.delete_employee
        )
        self.delete_button.grid(row=9, column=1, sticky="we")

        self.modify_button = tk.Button(self.master, text="Modify Employee", command=self.modify_employee)
        self.modify_button.grid(row=10, column=0, sticky="we")

        self.display_button = tk.Button(
            self.master, text="Display Employee", command=self.display_employee
        )
        self.display_button.grid(row=10, column=1, sticky="we")

        self.display_all_button = tk.Button(self.master, text="Display All Employee", command=self.display_all_employees)
        self.display_all_button.grid(row=11, columnspan=2, column=0, sticky="we")

    def add_employee(self):
        try:
            new_employee = Employee(
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
            self.employee_management.add_employee(new_employee)
            messagebox.showinfo("Success", "Employee added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not add employee: {e}")

    def delete_employee(self):
        employee_id = self.employee_id_entry.get()
        try:
            self.employee_management.delete_employee(employee_id)
            messagebox.showinfo("Success", "Employee deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete employee: {e}")

    def modify_employee(self):
        employee_id = self.employee_id_entry.get()
        try:
            self.employee_management.modify_employee(
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
            messagebox.showinfo("Success", "Employee modified successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not modify employee: {e}")

    def display_employee(self):
        employee_id = self.employee_id_entry.get()
        try:
            employee = self.employee_management.get_employee(employee_id)
            employee_info = (
                f"Name: {employee.name}\n"
                f"Department: {employee.department}\n"
                f"Job Title: {employee.job_title}\n"
                f"Basic Salary: {employee.basic_salary}\n"
                f"Age: {employee.age}\n"
                f"Date of Birth: {employee.date_of_birth}\n"
                f"Passport Details: {employee.passport_details}\n"
                f"Manager ID: {employee.manager_id}"
            )
            messagebox.showinfo("Employee Details", employee_info)
        except Exception as e:
            messagebox.showerror("Error", f"Could not display employee: {e}")

    def display_all_employees(self):
        try:
            all_employees_info = self.employee_management.display_all_employees()
            if all_employees_info:
                messagebox.showinfo("All Employees Details", all_employees_info)
            else:
                messagebox.showinfo("All Employees Details", "No employees to display.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

class ManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Events Company Management System")
        self.geometry("500x400")

        self.tab_control = ttk.Notebook(self)
        self.init_tabs()
        self.tab_control.pack(expand=1, fill="both")

    def init_tabs(self):
        self.client_tab = ttk.Frame(self.tab_control)
        self.client_gui = ClientGUI(self.client_tab)
        self.client_tab.pack(fill="both", expand=True)
        self.tab_control.add(self.client_tab, text="Clients")

        # Employee Tab
        self.employee_tab = ttk.Frame(self.tab_control)
        self.employee_gui = EmployeeGUI(self.employee_tab)
        self.employee_tab.pack(fill="both", expand=True)
        self.tab_control.add(self.employee_tab, text="Employees")

        # Event Tab
        self.event_tab = ttk.Frame(self.tab_control)
        self.event_gui = EventGUI(self.event_tab)
        self.event_tab.pack(fill="both", expand=True)
        self.tab_control.add(self.event_tab, text="Events")

        # Guest Tab
        self.guest_tab = ttk.Frame(self.tab_control)
        self.guest_gui = GuestGUI(self.guest_tab)
        self.guest_tab.pack(fill="both", expand=True)
        self.tab_control.add(self.guest_tab, text="Guests")

        # Supplier Tab
        self.supplier_tab = ttk.Frame(self.tab_control)
        self.supplier_gui = SupplierGUI(self.supplier_tab)
        self.supplier_tab.pack(fill="both", expand=True)
        self.tab_control.add(self.supplier_tab, text="Suppliers")

        # Venue Tab
        self.venue_tab = ttk.Frame(self.tab_control)
        self.venue_gui = VenueGUI(self.venue_tab)
        self.venue_tab.pack(fill="both", expand=True)
        self.tab_control.add(self.venue_tab, text="Venues")





if __name__ == "__main__":
    app = ManagementApp()
    app.mainloop()

