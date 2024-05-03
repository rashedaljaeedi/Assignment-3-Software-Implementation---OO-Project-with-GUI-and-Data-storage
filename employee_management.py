# employee_management.py
import os
import pickle

EMPLOYEE_FILE_PATH = "employees.bin"

class Employee:
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
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details
        self.manager_id = manager_id  # Stores the ID of the manager, if applicable

# Manager class inheriting from Employee
class Manager(Employee):
    # Extends Employee with attributes specific to a Manager's responsibilities.
    def __init__(self, team_size, department_budget, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Calls the constructor of the Employee class
        self.team_size = team_size  # Size of the team the manager is responsible for
        self.department_budget = department_budget  # Budget managed by the Manager

# Salesperson class inheriting from Employee
class Salesperson(Employee):
    # Extends Employee with attributes specific to a Salesperson's job role.
    def __init__(self, sales_target, commission_rate, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Calls the constructor of the Employee class
        self.sales_target = sales_target  # The sales target that the Salesperson must achieve
        self.commission_rate = commission_rate  # Commission rate for the Salesperson


class EmployeeManagement:
    def __init__(self):
        self.employees = self.load_employees()

    def load_employees(self):
        if os.path.exists(EMPLOYEE_FILE_PATH):
            with open(EMPLOYEE_FILE_PATH, "rb") as file:
                return pickle.load(file)
        return {}

    def save_employees(self):
        with open(EMPLOYEE_FILE_PATH, "wb") as file:
            pickle.dump(self.employees, file)

    def add_employee(self, employee):
        if employee.employee_id in self.employees:
            raise Exception("Employee ID already exists.")
        self.employees[employee.employee_id] = employee
        self.save_employees()

    def delete_employee(self, employee_id):
        if employee_id not in self.employees:
            raise Exception("Employee not found.")
        del self.employees[employee_id]
        self.save_employees()

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
    ):
        if employee_id not in self.employees:
            raise Exception("Employee not found.")
        employee = self.employees[employee_id]
        if name is not None:
            employee.name = name
        if department is not None:
            employee.department = department
        if job_title is not None:
            employee.job_title = job_title
        if basic_salary is not None:
            employee.basic_salary = basic_salary
        if age is not None:
            employee.age = age
        if date_of_birth is not None:
            employee.date_of_birth = date_of_birth
        if passport_details is not None:
            employee.passport_details = passport_details
        if manager_id is not None:
            employee.manager_id = manager_id
        self.save_employees()

    def get_employee(self, employee_id):
        if employee_id not in self.employees:
            raise Exception("Employee not found.")
        return self.employees[employee_id]

    def display_employee(self, employee_id):
        employee = self.get_employee(employee_id)
        print(f"Name: {employee.name}")
        print(f"ID Number: {employee.employee_id}")
        print(f"Department: {employee.department}")
        print(f"Job Title: {employee.job_title}")
        print(f"Basic Salary: {employee.basic_salary}")
        print(f"Age: {employee.age}")
        print(f"Date of Birth: {employee.date_of_birth}")
        print(f"Passport Details: {employee.passport_details}")
        if employee.manager_id:
            print(f"Manager ID: {employee.manager_id}")

    def display_all_employees(self):
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
                if employee.manager_id:
                    all_employees_info += f"Manager ID: {employee.manager_id}\n\n"  # Adding employee manager ID to the string if it exists
                else:
                    all_employees_info += "\n"  # Adding a blank line if there's no manager ID
            return all_employees_info  # Returning the string containing all employees' information

