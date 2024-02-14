# This is a submisionn of Pierre Ntakirutimana(pntakiru) and Leonard Niyiregeka (lniyiteg)
import json

class Employee:
    """This class helps us to keep information about employees of a company. It will also guide
    in calculating the earnings of the employee.
    Attributes:
        - employee_id (str): The unique identifier for the employee.
        - first_name (str): The first name of the employee.
        - last_name (str): The last name of the employee.
        - email (str): The email address of the employee.
        - salary (float): The salary of the employee.

    returns: Employee Object
    """
    import os
    os.system("cls")
    def __init__(self, employee_id,  first_name, last_name, email, base_salary):
        """Emplayerr class contructors"""
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__base_salary = base_salary

    @property
    def get_employee_id(self):
        """Employee ID getter
        args: None
        returns: employee_id
        """
        return self.__employee_id
    
    @get_employee_id.setter
    def set_employee_id(self, employee_id):
        """Employee ID setter
        args: employee_id
        returns: None
        """
        self.__employee_id = employee_id

    @property
    def get_first_name(self):
        """First Name getter
        args: None
        returns: first_name
        """
        return self.__first_name
    
    @get_first_name.setter
    def set_first_name(self, first_name):
        """First Name setter
        args: first_name
        returns: None
        """
        self.__first_name = first_name
        
    @property   
    def get_last_name(self):
        """Last Name getter
        args: None
        returns: last_name
        """
        return self.__last_name
    
    @get_last_name.setter
    def set_last_name(self, last_name):
        """Last Name setter
        args: last_name
        returns: None
        """
        self.__last_name = last_name

    @property
    def get_email(self):
        """Email getter
        args: None
        returns: email
        """
        return self.__email
    
    @get_email.setter
    def set_email(self, email):
        """Email setter
        args: email
        returns: None
        """
        self.__email = email

    @property
    def get_base_salary(self):
        """Salary getter
        args: None
        returns: salary
        """
        return self.__base_salary
    
    @get_base_salary.setter
    def set_base_salary(self, base_salary):
        """Salary setter
        args: salary
        returns: None
        """
        self.__base_salary = base_salary
    
    def calculate_earnings(self):
        """Calculate earnings method
        args: none
        returns: total earnings of the employee with the given ratio of the salary
        """
        return self.get_base_salary
    
        

    def __str__(self) -> str:  
        return f"""Your employee details are:\n ID: {self.__employee_id:>0}\n First Name: {self.__first_name}\n Last Name:  {self.__last_name:<0}\n Email: {self.__email}\n"""
    


# employee_1 = Employee("1", "Peter", "Parker", "XXXXXXXXXXXXXXXXXXXXX", 2000)
# print(employee_1)


