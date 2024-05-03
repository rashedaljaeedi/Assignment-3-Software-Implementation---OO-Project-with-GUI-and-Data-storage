import os  # Importing the os module for operating system related functionalities
import pickle  # Importing the pickle module for object serialization

EMPLOYEE_FILE_PATH = "employees.bin"  # File path constant for storing employee data

class Employee:  # Definition of the Employee class
    # Initializes an Employee object with personal and job-related attributes.
    def __init__(
            self,
            name,
            employee_id,
            department,
            job_title,
            basic_salary,
            age,
            date_of_birth,
            passport_details,
            manager_id=None,  # Optional attribute; defaults to None if not provided
    ):
        self.name = name  # Name of the employee
        self.employee_id = employee_id  # Unique identifier for the employee
        self.department = department  # Department of the employee
        self.job_title = job_title  # Job title of the employee
        self.basic_salary = basic_salary  # Basic salary of the employee
        self.age = age  # Age of the employee
        self.date_of_birth = date_of_birth  # Date of birth of the employee
        self.passport_details = passport_details  # Passport details of the employee
        self.manager_id = manager_id  # Stores the ID of the manager, if applicable

class EmployeeManagement:  # Definition of the EmployeeManagement class
    def __init__(self):  # Constructor method for initializing employee management instance
        self.employees = self.load_employees()  # Loading employees data when an instance is created

    def load_employees(self):  # Method for loading employees data from file
        """
        Load employees from the binary file if it exists.
        Returns:
            dict: A dictionary containing loaded employee data.
        """
        if os.path.exists(EMPLOYEE_FILE_PATH):  # Checking if the file exists
            with open(EMPLOYEE_FILE_PATH, "rb") as file:  # Opening the file in binary read mode
                try:
                    return pickle.load(file)  # Loading data from the file using pickle
                except (pickle.UnpicklingError, EOFError) as e:  # Handling errors during unpickling
                    print(f"Error loading employees data: {e}")  # Printing error message
                    return {}  # Returning an empty dictionary if error occurs
        return {}  # Returning an empty dictionary if file doesn't exist

    def save_employees(self):  # Method for saving employees data to file
        with open(EMPLOYEE_FILE_PATH, "wb") as file:  # Opening the file in binary write mode
            pickle.dump(self.employees, file)  # Saving data to the file using pickle

    def add_employee(self, employee):  # Method for adding a new employee
        if employee.employee_id in self.employees:  # Checking if employee ID already exists
            raise ValueError("Employee ID already exists.")  # Raising an error if employee ID is not unique
        self.employees[employee.employee_id] = employee  # Adding the new employee to the employees dictionary
        self.save_employees()  # Saving the updated employees data to file

    def delete_employee(self, employee_id):  # Method for deleting an employee
        if employee_id not in self.employees:  # Checking if employee ID exists
            raise ValueError("Employee not found.")  # Raising an error if employee ID doesn't exist
        del self.employees[employee_id]  # Deleting the employee from the employees dictionary
        self.save_employees()  # Saving the updated employees data to file

    def modify_employee(
            self,
            employee_id,
            name=None,
            department=None,
            job_title=None,
            basic_salary=None,
            age=None,
            date_of_birth=None,
            passport_details=None,
            manager_id=None,
    ):  # Method for modifying employee attributes
        if employee_id not in self.employees:  # Checking if employee ID exists
            raise ValueError("Employee not found.")  # Raising an error if employee ID doesn't exist
        employee = self.employees[employee_id]  # Getting the employee object
        if name is not None:  # Checking if name attribute is provided
            employee.name = name  # Setting the new value for the name attribute
        if department is not None:  # Checking if department attribute is provided
            employee.department = department  # Setting the new value for the department attribute
        if job_title is not None:  # Checking if job_title attribute is provided
            employee.job_title = job_title  # Setting the new value for the job_title attribute
        if basic_salary is not None:  # Checking if basic_salary attribute is provided
            employee.basic_salary = basic_salary  # Setting the new value for the basic_salary attribute
        if age is not None:  # Checking if age attribute is provided
            employee.age = age  # Setting the new value for the age attribute
        if date_of_birth is not None:  # Checking if date_of_birth attribute is provided
            employee.date_of_birth = date_of_birth  # Setting the new value for the date_of_birth attribute
        if passport_details is not None:  # Checking if passport_details attribute is provided
            employee.passport_details = passport_details  # Setting the new value for the passport_details attribute
        if manager_id is not None:  # Checking if manager_id attribute is provided
            employee.manager_id = manager_id  # Setting the new value for the manager_id attribute
        self.save_employees()  # Saving the updated employees data to file

    def get_employee(self, employee_id):  # Method for retrieving an employee
        if employee_id not in self.employees:  # Checking if employee ID exists
            raise ValueError("Employee not found.")  # Raising an error if employee ID doesn't exist
        return self.employees[employee_id]  # Returning the employee object

    def display_employee(self, employee_id):  # Method for displaying details of a specific employee
        employee = self.get_employee(employee_id)  # Getting the employee object
        print(f"Name: {employee.name}")  # Displaying employee name
        print(f"ID Number: {employee.employee_id}")  # Displaying employee ID
        print(f"Department: {employee.department}")  # Displaying employee department
        print(f"Job Title: {employee.job_title}")  # Displaying employee job title
        print(f"Basic Salary: {employee.basic_salary}")  # Displaying employee basic salary
        print(f"Age: {employee.age}")  # Displaying employee age
        print(f"Date of Birth: {employee.date_of_birth}")  # Displaying employee date of birth
        print(f"Passport Details: {employee.passport_details}")  # Displaying employee passport details
        if employee.manager_id:  # Checking if manager ID exists
            print(f"Manager ID: {employee.manager_id}")  # Displaying employee manager ID

    def display_all_employees(self):  # Method for displaying details of all employees
        if not self.employees:  # Checking if employees dictionary is empty
            return "No employees to display."  # Returning message if no employees exist
        else:
            all_employees_info = ""  # Initializing string to store all employees' information
            for employee_id, employee in self.employees.items():  # Iterating over employees dictionary
                all_employees_info += f"Employee ID: {employee_id}\n"  # Adding employee ID to the string
                all_employees_info += f"Name: {employee.name}\n"  # Adding employee name to the string
                all_employees_info += f"Department: {employee.department}\n"  # Adding employee department to the string
                all_employees_info += f"Job Title: {employee.job_title}\n"  # Adding employee job title to the string
                all_employees_info += f"Basic Salary: {employee.basic_salary}\n"  # Adding employee basic salary to the string
                all_employees_info += f"Age: {employee.age}\n"  # Adding employee age to the string
                all_employees_info += f"Date of Birth: {employee.date_of_birth}\n"  # Adding employee date of birth to the string
                all_employees_info += f"Passport Details: {employee.passport_details}\n"  # Adding employee passport details to the string
                if employee.manager_id:  # Checking if manager ID exists
                    all_employees_info += f"Manager ID: {employee.manager_id}\n\n"  # Adding employee manager ID to the string if it exists
                else:
                    all_employees_info += "\n"  # Adding a blank line if there's no manager ID
            return all_employees_info  # Returning the string containing all employees' information
