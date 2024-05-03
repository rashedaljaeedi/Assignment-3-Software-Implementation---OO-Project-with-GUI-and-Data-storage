import os  # Importing the os module for operating system related functionalities
import pickle  # Importing the pickle module for object serialization

CLIENT_FILE_PATH = "clients.txt"  # File path constant for storing client data

class Client:  # Definition of the Client class
    def __init__(self, client_id, name, address, contact_details, budget):  # Constructor method for initializing client attributes
        self.client_id = client_id  # Assigning client ID
        self.name = name  # Assigning client name
        self.address = address  # Assigning client address
        self.contact_details = contact_details  # Assigning client contact details
        self.budget = budget  # Assigning client budget

class ClientManagement:  # Definition of the ClientManagement class
    def __init__(self):  # Constructor method for initializing client management instance
        self.clients = self.load_clients()  # Loading clients data when an instance is created

    def load_clients(self):  # Method for loading clients data from file
        if os.path.exists(CLIENT_FILE_PATH):  # Checking if the file exists
            with open(CLIENT_FILE_PATH, "rb") as file:  # Opening the file in binary read mode
                try:
                    return pickle.load(file)  # Loading data from the file using pickle
                except (pickle.UnpicklingError, EOFError) as e:  # Handling errors during unpickling
                    print(f"Error loading clients data: {e}")  # Printing error message
                    return {}  # Returning an empty dictionary if error occurs
        return {}  # Returning an empty dictionary if file doesn't exist

    def save_clients(self):  # Method for saving clients data to file
        with open(CLIENT_FILE_PATH, "wb") as file:  # Opening the file in binary write mode
            pickle.dump(self.clients, file)  # Saving data to the file using pickle

    def add_client(self, client):  # Method for adding a new client
        if client.client_id in self.clients:  # Checking if client ID already exists
            raise ValueError("Client ID already exists.")  # Raising an error if client ID is not unique
        self.clients[client.client_id] = client  # Adding the new client to the clients dictionary
        self.save_clients()  # Saving the updated clients data to file

    def delete_client(self, client_id):  # Method for deleting a client
        if client_id not in self.clients:  # Checking if client ID exists
            raise ValueError("Client not found.")  # Raising an error if client ID doesn't exist
        del self.clients[client_id]  # Deleting the client from the clients dictionary
        self.save_clients()  # Saving the updated clients data to file

    def modify_client(self, client_id, **kwargs):  # Method for modifying client attributes
        if client_id not in self.clients:  # Checking if client ID exists
            raise ValueError("Client not found.")  # Raising an error if client ID doesn't exist
        client = self.clients[client_id]  # Getting the client object
        allowed_attributes = set(['name', 'address', 'contact_details', 'budget'])  # Allowed attributes for modification
        for key, value in kwargs.items():  # Iterating over keyword arguments
            if key not in allowed_attributes:  # Checking if attribute is allowed for modification
                raise ValueError(f"{key} is not a valid attribute of Client.")  # Raising an error for invalid attribute
            setattr(client, key, value)  # Setting the new value for the attribute
        self.save_clients()  # Saving the updated clients data to file

    def get_client(self, client_id):  # Method for retrieving a client
        if client_id not in self.clients:  # Checking if client ID exists
            raise ValueError("Client not found.")  # Raising an error if client ID doesn't exist
        return self.clients[client_id]  # Returning the client object

    def display_client(self, client_id):  # Method for displaying details of a specific client
        client = self.get_client(client_id)  # Getting the client object
        print(f"Client ID: {client.client_id}")  # Displaying client ID
        print(f"Name: {client.name}")  # Displaying client name
        print(f"Address: {client.address}")  # Displaying client address
        print(f"Contact Details: {client.contact_details}")  # Displaying client contact details
        print(f"Budget: {client.budget}")  # Displaying client budget

    def display_all_clients(self):  # Method for displaying details of all clients
        if not self.clients:  # Checking if clients dictionary is empty
            return "No clients to display."  # Returning message if no clients exist
        else:
            all_clients_info = ""  # Initializing string to store all clients' information
            for client_id, client in self.clients.items():  # Iterating over clients dictionary
                all_clients_info += f"Client ID: {client_id}\n"  # Adding client ID to the string
                all_clients_info += f"Name: {client.name}\n"  # Adding client name to the string
                all_clients_info += f"Address: {client.address}\n"  # Adding client address to the string
                all_clients_info += f"Contact Details: {client.contact_details}\n"  # Adding client contact details to the string
                all_clients_info += f"Budget: {client.budget}\n\n"  # Adding client budget to the string
            return all_clients_info  # Returning the string containing all clients' information
