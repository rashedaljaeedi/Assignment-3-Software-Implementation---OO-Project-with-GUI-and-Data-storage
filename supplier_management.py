# supplier_management.py
import os
import pickle

SUPPLIER_FILE_PATH = "suppliers.bin"

class Supplier:
    # Initializes a Supplier object who provides services for events.
    def __init__(self, supplier_id, name, address, contact_details, service_provided):
        self.supplier_id = supplier_id  # Unique identifier for the supplier
        self.name = name  # Name of the supplier company
        self.address = address  # Address of the supplier
        self.contact_details = contact_details  # Contact details for the supplier
        self.service_provided = service_provided  # Services that the supplier provides


class SupplierManagement:
    def __init__(self):
        self.suppliers = self.load_suppliers()

    def load_suppliers(self):
        if os.path.exists(SUPPLIER_FILE_PATH):
            with open(SUPPLIER_FILE_PATH, "rb") as file:
                return pickle.load(file)
        return {}

    def save_suppliers(self):
        with open(SUPPLIER_FILE_PATH, "wb") as file:
            pickle.dump(self.suppliers, file)

    def add_supplier(self, supplier):
        if supplier.supplier_id in self.suppliers:
            raise Exception("Supplier ID already exists.")
        self.suppliers[supplier.supplier_id] = supplier
        self.save_suppliers()

    def delete_supplier(self, supplier_id):
        if supplier_id not in self.suppliers:
            raise Exception("Supplier not found.")
        del self.suppliers[supplier_id]
        self.save_suppliers()

    def modify_supplier(self, supplier_id, **kwargs):
        if supplier_id not in self.suppliers:
            raise Exception("Supplier not found.")
        supplier = self.suppliers[supplier_id]
        for key, value in kwargs.items():
            if hasattr(supplier, key):
                setattr(supplier, key, value)
            else:
                raise Exception(f"{key} is not a valid attribute of Supplier.")
        self.save_suppliers()

    def get_supplier(self, supplier_id):
        if supplier_id not in self.suppliers:
            raise Exception("Supplier not found.")
        return self.suppliers[supplier_id]

    def display_supplier(self, supplier_id):
        supplier = self.get_supplier(supplier_id)
        print(f"Supplier ID: {supplier.supplier_id}")
        print(f"Name: {supplier.name}")
        print(f"Address: {supplier.address}")
        print(f"Contact Details: {supplier.contact_details}")
        print(f"Service Provided: {supplier.service_provided}")

    def display_all_suppliers(self):
        if not self.suppliers:
            return "No suppliers to display."
        else:
            all_suppliers_info = ""
            for supplier_id, supplier in self.suppliers.items():
                all_suppliers_info += f"Supplier ID: {supplier.supplier_id}\n"
                all_suppliers_info += f"Name: {supplier.name}\n"
                all_suppliers_info += f"Address: {supplier.address}\n"
                all_suppliers_info += f"Contact Details: {supplier.contact_details}\n"
                all_suppliers_info += f"Service Provided: {supplier.service_provided}\n\n"
            return all_suppliers_info

