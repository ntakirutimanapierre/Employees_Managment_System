from Employee import Employee

class Manager(Employee):
    """This is a class of managerm emmployee, that inherit from Employee class and add depatment name and number of direct report
    args: 
    Attributes:
        - employee_id (str): The unique identifier for the manager.
        - first_name (str): The first name of the manager.
        - last_name (str): The last name of the manager.
        - email (str): The email address of the manager.
        - salary (float): The base salary of the manager.
        - department_name (str): The name of the department the manager is managing.
        - number_of_direct_reports (int): The number of direct reports the manager manages.
    return: Manager Object
    """
    def __init__(self,employee_id,
                   first_name, 
                   last_name, 
                   email, 
                   salary, 
                   department_name,
                   number_of_direct_reports):
        super().__init__(employee_id,  first_name, last_name, email, salary)
        self.__department_name = department_name
        self.__number_of_direct_reports = number_of_direct_reports

    @property    
    def get_department_name(self):
        """Department getter
        args: none
        returns: department name
        """
        return self.__department_name
    
    @get_department_name.setter
    def set_department_name(self, department_name):
        """Department setter
        args: department name
        returns: none
        """
        self.__department_name = department_name

    @property
    def get_number_of_direct_reports(self):
        """Number of direct reports getter
        args: none
        returns: number of direct reports
        """
        return self.__number_of_direct_reports
    
    @get_number_of_direct_reports.setter
    def set_number_of_direct_reports(self, number_of_direct_reports):
        """Number of direct reports setter
        args: number of direct reports
        returns: none
        """
        self.__number_of_direct_reports = number_of_direct_reports

    def total_earning(self, rate):
        """Calculate total earnings of the manager
        args: rate
        returns: total earnings of the manager
        """
        if 0 <= rate <= 60:
            return super().calculate_earnings()*(1+rate/100)
        else:
            raise ValueError("Invalid rate, that valid rate must be between 0 and 60")
        
    def __str__(self) -> str:
        rate = eval(input("Enter the rate: "))
        return super().__str__()+f"""\n Department Name: {self.__department_name}\n Number of Direct Reports: {self.__number_of_direct_reports}\n Total Earning: {self.total_earning(rate)}"""

def __main__():
    a = Manager("QLA2356", "Angeline", "Abayo", "abayo@chs.rw", 120, "Business Strategy", 4)
    print('___________________________________')
    print(a.__str__())
    print('___________________________________\n')

    a.set_department_name = "Marketing"
    print(a)

# __main__()