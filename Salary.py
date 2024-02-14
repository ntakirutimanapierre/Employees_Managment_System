# import the required external modules
import json
import numpy as np
from Intern import Intern
from Manager import Manager
from Director import Director
import os
from datetime import datetime

class Salary:
    """this is salary class which deals with calcultig salary appropriately according to the type of the employee
        """
    def __init__(self, employee_db_file, salary_data_file, employee_id):

        """ salary constuctor definition to allow initialization of object of salary class"""
        self.employee_db_file = employee_db_file
        self.salary_data_file = salary_data_file
        self.employee_id = employee_id

    def load_employee_db(self):
        """this methods has function of loading employee database and returning the file or 
        releasing appropriate error message just in case there is an error  
        Args: none
        Returns: employees from employee database
        
        """
        try:
            with open(self.employee_db_file, "r") as file:
                content = json.load(file)
            if self.employee_id not in content:
                raise ValueError("Employee ID not found in the database\n")
            else:
                return content
        except FileNotFoundError:
            os.system("cls")    
            print("Exiting... Employee database file not found.")
            exit()
            

    def load_salary_data(self):
        """this method has function of reading the salary database to check the salary history for the employee
        Args: None
        RETURNS: darta from the salary database 
        """
        try:
            with open(self.salary_data_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Salary data file not found.")
            return False

    def calculate_salary_per_employee_type(self):
        """ this is the method which calculate the salary of the employee according to their types
            args: none
            returns: the salary of the employee
        """

        employee_db = self.load_employee_db()
        if self.employee_id in employee_db:
            employee_data = employee_db[self.employee_id]
            employee_type = employee_data.get("Job Level")

            if employee_type == "Intern":
                # Assuming you have director_attributes obtained from employee_data.values()
                intern_attributes = list(employee_data.values())  # Convert it to a list
                intern_attributes = intern_attributes[:-1]  # Slice to remove the last element
                intern_attributes = tuple(intern_attributes)  # Convert back to a tuple (if needed)
                intern = Intern(self.employee_id, *intern_attributes)
                return intern.total_earning()
            elif employee_type == "Manager":
                manager_attributes = list(employee_data.values())  # Convert it to a list
                manager_attributes = manager_attributes[:-1]  # Slice to remove the last element
                manager_attributes = tuple(manager_attributes)  # Convert back to a tuple (if needed)
                manager = Manager(self.employee_id,
                                 *manager_attributes
                                 )


                rate = float(input(f"Employee {self.employee_id} is a manager, please enter allowance rate: "))
                return manager.total_earning(rate)
            elif employee_type == "Director":

                # Assuming you have director_attributes obtained from employee_data.values()
                director_attributes = list(employee_data.values())  # Convert it to a list
                director_attributes = director_attributes[:-1]  # Slice to remove the last element
                director_attributes = tuple(director_attributes)  # Convert back to a tuple (if needed)

                director = Director(self.employee_id,
                                     *director_attributes
                                     )
                return director.calculate_pay()
            else:
                raise ValueError("Invalid employee type")
        else:
            raise ValueError("Employee not found in the database")


    def allowance(self):
        """this method calculates the allowance of the employee according to the agreed up on rate"""
        employee_db = self.load_employee_db()
        base_salary = employee_db[self.employee_id].get("base salary")
        return base_salary / 12 * 0.05

    def tax(self):
        employee_db = self.load_employee_db()
        base_salary = employee_db[self.employee_id].get("base salary")
        return np.round((base_salary * 0.3) / 12, 2)

    def bonus(self, check = True):
        employee_db = self.load_employee_db()
        if check:
            base_salary = employee_db[self.employee_id].get("base salary")
            return np.round((base_salary * 0.01) / 12, 2)
        return 0

    def net_salary(self):
        return self.calculate_salary_per_employee_type() - self.tax() + self.bonus()

    def save_salary_data(self):
        """ this is the method that saves the salary information of the employee in the salary database."""
        current_datetime = datetime.now()
        employee_db = self.load_employee_db()

        formatted_timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        salary_breakdown = {
            "Base Salary": employee_db[self.employee_id].get("base salary"),
            "Tax": self.tax(),
            "Allowance": self.allowance(),
            "Bonus": self.bonus(),
            "Net Salary": self.net_salary()
        }

        try:
            with open(self.salary_data_file, "r") as file:
                salary_data = json.load(file)
            if self.employee_id in salary_data:
                salary_data[self.employee_id].append({formatted_timestamp: salary_breakdown})
            else:
                salary_data[self.employee_id] = [{formatted_timestamp: salary_breakdown}]
        except FileNotFoundError:
            salary_data = {
                self.employee_id: [{formatted_timestamp: salary_breakdown}]
            }

        with open(self.salary_data_file, "w") as file:
            json.dump(salary_data, file)
# define the main function for this class.
    def __main__(self):
        try:
            self.save_salary_data()
            os.system('cls')
            print("Salary data saved successfully.")
        except ValueError as e:
            print(f"Error: {e}")
