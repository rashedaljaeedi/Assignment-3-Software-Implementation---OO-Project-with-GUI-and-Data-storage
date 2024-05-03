import os  # Importing the os module for operating system related functionalities
import pickle  # Importing the pickle module for object serialization

SUPPLIER_FILE_PATH = "suppliers.bin"  # File path constant for storing supplier data

class Supplier:  # Definition of the Supplier class
    # Initializes a Supplier object who provides services for events.
    def __init__(self, supplier_id, name, address, contact_details, service_provided,min_guests_supplier, max_guests_supplier, menu):
        self.supplier_id = supplier_id  # Unique identifier for the supplier
        self.name = name  # Name of the supplier company
        self.address = address  # Address of the supplier
        self.contact_details = contact_details  # Contact details for the supplier
        self.service_provided = service_provided  # Services that the supplier provides
        self.min_guests_supplier = min_guests_supplier # Minimum number of guests the supplier or  can accommodate
        self.max_guests_supplier = max_guests_supplier  # Maximum number of guests the venue can accommodate
        self.menu = menu  # Menu offered by the supplier
class SupplierManagement:  # Definition of the SupplierManagement class
    def __init__(self):  # Constructor method for initializing supplier management instance
        self.suppliers = self.load_suppliers()  # Loading suppliers data when an instance is created

    def load_suppliers(self):  # Method for loading suppliers data from file
        if os.path.exists(SUPPLIER_FILE_PATH):  # Checking if the file exists
            with open(SUPPLIER_FILE_PATH, "rb") as file:  # Opening the file in binary read mode
                try:
                    return pickle.load(file)  # Loading data from the file using pickle
                except (pickle.UnpicklingError, EOFError) as e:  # Handling errors during unpickling
                    print(f"Error loading suppliers data: {e}")  # Printing error message
                    return {}  # Returning an empty dictionary if error occurs
        return {}  # Returning an empty dictionary if file doesn't exist

    def save_suppliers(self):  # Method for saving suppliers data to file
        with open(SUPPLIER_FILE_PATH, "wb") as file:  # Opening the file in binary write mode
            pickle.dump(self.suppliers, file)  # Saving data to the file using pickle

    def add_supplier(self, supplier):  # Method for adding a new supplier
        if supplier.supplier_id in self.suppliers:  # Checking if supplier ID already exists
            raise Exception("Supplier ID already exists.")  # Raising an error if supplier ID is not unique
        self.suppliers[supplier.supplier_id] = supplier  # Adding the new supplier to the suppliers dictionary
        self.save_suppliers()  # Saving the updated suppliers data to file

    def delete_supplier(self, supplier_id):  # Method for deleting a supplier
        if supplier_id not in self.suppliers:  # Checking if supplier ID exists
            raise Exception("Supplier not found.")  # Raising an error if supplier ID doesn't exist
        del self.suppliers[supplier_id]  # Deleting the supplier from the suppliers dictionary
        self.save_suppliers()  # Saving the updated suppliers data to file

    def modify_supplier(self, supplier_id, **kwargs):  # Method for modifying supplier attributes
        if supplier_id not in self.suppliers:  # Checking if supplier ID exists
            raise Exception("Supplier not found.")  # Raising an error if supplier ID doesn't exist
        supplier = self.suppliers[supplier_id]  # Getting the supplier object
        for key, value in kwargs.items():  # Iterating over keyword arguments
            if hasattr(supplier, key):  # Checking if the supplier has the attribute
                setattr(supplier, key, value)  # Setting the new value for the attribute
            else:
                raise Exception(f"{key} is not a valid attribute of Supplier.")  # Raising an error for invalid attribute
        self.save_suppliers()  # Saving the updated suppliers data to file

    def get_supplier(self, supplier_id):  # Method for retrieving a supplier
        if supplier_id not in self.suppliers:  # Checking if supplier ID exists
            raise Exception("Supplier not found.")  # Raising an error if supplier ID doesn't exist
        return self.suppliers[supplier_id]  # Returning the supplier object

    def display_supplier(self, supplier_id):  # Method for displaying details of a specific supplier
        supplier = self.get_supplier(supplier_id)  # Getting the supplier object
        print(f"Supplier ID: {supplier.supplier_id}")  # Displaying supplier ID
        print(f"Name: {supplier.name}")  # Displaying supplier name
        print(f"Address: {supplier.address}")  # Displaying supplier address
        print(f"Contact Details: {supplier.contact_details}")  # Displaying supplier contact details
        print(f"Service Provided: {supplier.service_provided}")  # Displaying supplier services provided
        print(f"Minimum Guests: {supplier.min_guests_supplier}")  # Displaying minimum guests
        print(f"Maximum Guests: {supplier.max_guests_supplier}")  # Displaying maximum guests
        print(f"Menu: {supplier.menu}")  # Displaying menu

    def display_all_suppliers(self):  # Method for displaying details of all suppliers
        if not self.suppliers:  # Checking if suppliers dictionary is empty
            return "No suppliers to display."  # Returning message if no suppliers exist
        else:
            all_suppliers_info = ""  # Initializing string to store all suppliers' information
            for supplier_id, supplier in self.suppliers.items():  # Iterating over suppliers dictionary
                all_suppliers_info += f"Supplier ID: {supplier_id}\n"  # Adding supplier ID to the string
                all_suppliers_info += f"Name: {supplier.name}\n"  # Adding supplier name to the string
                all_suppliers_info += f"Address: {supplier.address}\n"  # Adding supplier address to the string
                all_suppliers_info += f"Contact Details: {supplier.contact_details}\n"  # Adding supplier contact details to the string
                all_suppliers_info += f"Service Provided: {supplier.service_provided}\n\n"  # Adding supplier services provided to the string
                all_suppliers_info += f"Minimum Guests: {supplier.min_guests_supplier}\n"  # Adding minimum guests to the string
                all_suppliers_info += f"Maximum Guests: {supplier.max_guests_supplier}\n\n"  # Adding maximum guests to the string
                all_suppliers_info += f"Menu: {supplier.menu}\n\n"  # Adding menu to the string
            return all_suppliers_info  # Returning the string containing all suppliers' information
