from Employee import Employee

class Intern(Employee):
    """This is an  Intern class, it inherits from Employee class and add few atributes to describe an intern.
    
    Attributes:
        - employee_id (str): The unique identifier for the intern.
        - first_name (str): The first name of the intern.
        - last_name (str): The last name of the intern.
        - email (str): The email address of the intern.
        - salary (float): The base salary of the intern.
        - university_name (str): The name of the university the intern is attending.
        - program_name (str): The name of the program the intern is attending.
        - internership_duration (int): The duration of the internship in months.
    returns: Intern object
    """
    def __init__(self,employee_id,
                first_name,
                last_name,
                email,
                salary,
                university_name,
                program_name,
                internership_duration
                ):
        
        super().__init__(employee_id,  first_name, last_name, email, salary)
        self.__university_name = university_name
        self.__program_name = program_name
        self.__internership_duration = internership_duration
        super().__init__(employee_id,  first_name, last_name, email, salary)

    @property
    def get_university_name(self):
        """University getter
        args: none
        returns: university name
        """
        return self.__university_name
    
    @get_university_name.setter
    def set_university_name(self, university_name):
        """University setter
        args: university name
        returns: none
        """
        self.__university_name = university_name
        
    @property
    def get_program_name(self):
        """Program name getter
        args: none
        returns: program name
        """
        return self.__program_name
    
    @get_program_name.setter
    def set_program_name(self, program_name):
        """program name setter
        args: program name
        returns: none
        """
        self.__program_name = program_name

    @property
    def get_internership_duration(self):
        """Internership duration getter
        args: none
        returns: internership duration
        """
        return self.__internership_duration
    
    @get_internership_duration.setter
    def set_internership_duration(self, internership_duration):
        """internership duration setter
        args: internership duration
        returns: none
        """
        if 3<=internership_duration<=6:
            self.__internership_duration = internership_duration
        else:
            raise ValueError("Invalid internership duration, that valid internership duration must be between 3 and 6 months")
        
    def total_earning(self):
        """Total earning getter
        args: none
        returns: total earning
        """
        if 3<= self.__internership_duration<=6:
            return super().calculate_earnings()*(self.__internership_duration/12)
        else:
            raise ValueError("Invalid internship duration it must be between(0 and 60)")

    def __str__(self):
        return super().__str__()+ f"\n Internship Duration: {self.__internership_duration} months\n University: {self.__university_name}\n Program: {self.__program_name}\n Earning: {self.total_earning()}"
    
def __main__():
    aaaa = Intern("QLA2356", "Angeline", "Abayo", "abayo@chs.rw", 120, "CMU", "MS ECE", 4)
    print('___________________________________')
    print(aaaa)
    print('___________________________________\n')


# __main__()
