from Employee import Employee

class Director(Employee):
    import os
    os.system("cls")
    """This class is used to represent a Director as an employee,
    It inherits from Employee class, and add two more arguments to it.
    Attributes:
        - employee_id (str): The unique identifier for the director.
        - first_name (str): The first name of the director.
        - last_name (str): The last name of the director.
        - email (str): The email address of the director.
        - salary (float): The salary of the director.
        - department (str): The department of the director.
        - annual_bonus (float): The annual bonus of the director.    
    return: Director Object
    """
    def __init__(self,employee_id,  first_name, last_name, email, salary, department, annual_bonus):
        super().__init__(employee_id,  first_name, last_name, email, salary)
        self.__department = department
        self.__annual_bonus = annual_bonus

    @property
    def get_department(self):
        """Department getter
        args: None
        returns: department
        """
        return self.__department
    
    @get_department.setter
    def set_department(self, department):
        """Department setter
        args: department
        returns: None
        """
        self.__department = department

    @property
    def get_annual_bonus(self):
        """Annual Bonus getter
        args: None
        returns: annual bonus
        """
        return self.__annual_bonus
    
    @get_annual_bonus.setter
    def set_annual_bonus(self, annual_bonus):
        """Annual Bonus setter
        args: annual bonus
        returns: None
        """
        self.__annual_bonus = annual_bonus

    def calculate_pay(self):
        """Calculate pay method
        args: None
        returns: total earnings of the employee with the given ratio of the salary
        """
        return super().calculate_earnings() + float(self.get_annual_bonus)


    def __str__(self) -> str:
        """String representation of the Director class
        args: None
        returns: String representation of the Director class
        """
        return super().__str__()+f"\n Department: {self.__department}\n Annual Bonus: {self.__annual_bonus}\n Total Pay: {self.calculate_pay()}"
    
def __main__(): 
    a = Director("QLA2356", "Angeline", "Abayo", "abayo@chs.rw", 120, "Business Strategy", 30)
    print('________________________________________')
    print(a)
    print('________________________________________\n')


#__main__()
