import json
import os
from datetime import datetime
os.system('cls')

class Attendance:

    """This class helps the HR mamnaager in attendance managemnet, it can perfrom three main taks
    1. Record entry date
    2. Record exit date
    3. Calculate total working hours for the durstion

    args: employee_database_file (str), attendance_file (str)
    returns: None
    """
    def __init__(self, employee_database_file, attendance_file): # Attenca class contructores

        self.employee_data = self.load_employee_data(employee_database_file)
        self.attendance_data = self.load_attendance_data(attendance_file)

    def load_employee_data(self, employee_database_file):
        """This is employee databae loader, it will chech is the emlpoyoyye database exist and take its content
        and transform them into dictionary, if the databse is not available it will raise"""
        try:
            with open(employee_database_file, "r") as file:
                content = json.load(file)
            return content
        
        except FileNotFoundError:
            print("Error: The employee database file is not found.")
            return {}
        
    

    def load_attendance_data(self, attendance_file):
        """This is employee databae loader, it will chech is the emlpoyoyye database exist and take its content
                and transform them into dictionary, if the databse is not available it will create an empty dictionary to 
                keep data"""
        try:
            with open(attendance_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            os.system('cls')
            print("Error: The attendance record file is not found.")
            return {}
        
    def is_valid_date(self, date):
        """Chech is the date entered is valied
        args: date in -dd-mm-yy
        return: True or False 
        
        """
        try:
            datetime.strptime(date, '%d-%m-%Y')
            return True
        except ValueError:
            os.system('cls')
            print("Invalid date: Enter a valid date in dd-MM-yyyy format.")
            return False

    def is_valid_time(self, time_str):
        """Chech is the time entered is valied
        args: time in -HH:MM
        return: True or False 
        
        """
        try:
            datetime.strptime(time_str, '%H:%M')
            return True
        except ValueError:
            os.system('cls')
            print("Invalid Time: Enter a valid time in HH:MM 24-hour format.")
            return False

    def record_entry(self, employee_id, entry_date, in_time):
        """This function will record entry date and time for the employee
        args: employee_id (str), entry_date (str), in_time (str)
        return: True or False 
        
        """
        if employee_id not in self.employee_data:
            os.system('cls')
            print("Error: There is no employee with the entered employee id.")
            return False

        if not self.is_valid_date(entry_date):
            return False

        if not self.is_valid_time(in_time):
            return False

        if employee_id in self.attendance_data:
            if entry_date in self.attendance_data[employee_id]:
                os.system('cls')
                
                print("Entry for the specified date already recorded.")
                return False
        else:
            self.attendance_data[employee_id] = {}

        self.attendance_data[employee_id][entry_date] = {"in-time": in_time}
        self.save_attendance_data()

        os.system('cls')
        print("Entry recorded successfully.")
        return True
    
    def record_exit(self, employee_id, exit_date, out_time):
        """This function will record exit date and time for the employee
        args: employee_id (str), exit_date (str), out_time (str)
        return: True or False 
        
        """
        if employee_id not in self.employee_data:
            os.system('cls')
            print("Error: There is no employee with the entered employee id.")
            return False

        if not self.is_valid_date(exit_date):
            return False

        if not self.is_valid_time(out_time):
            return False

        if employee_id in self.attendance_data:
            if exit_date not in self.attendance_data[employee_id]:
                os.system('cls')
                print("Entry for the specified date not found. Please record the entry first.")
                return False
        else:
            print("Entry for the specified date not found. Please record the entry first.")
            return False

        if "out-time" in self.attendance_data[employee_id][exit_date]:
            print("Exit for the specified date already recorded.")
            return False

        self.attendance_data[employee_id][exit_date]["out-time"] = out_time
        self.save_attendance_data()

        os.system('cls')
        print("Exit recorded successfully.")
        return True
    
    def calculate_working_hours(self, employee_id, start_date, end_date):
        """This function will calculate total working hours for the employee
        args: employee_id (str), start_date (str), end_date (str)
        return: working hours (float)
        
        """
        if employee_id not in self.employee_data:
            os.system('cls')
            print("Error: There is no employee with the entered employee id.")
            return None

        if not self.is_valid_date(start_date) or not self.is_valid_date(end_date):
            return None

        if employee_id in self.attendance_data:
            working_hours = 0.0

            for entry_date, data in self.attendance_data[employee_id].items():
                entry_datetime = datetime.strptime(entry_date, '%d-%m-%Y')
                start_datetime = datetime.strptime(start_date, '%d-%m-%Y')
                end_datetime = datetime.strptime(end_date, '%d-%m-%Y')

                if start_datetime <= entry_datetime <= end_datetime:
                    in_time = datetime.strptime(data.get("in-time", "00:00"), '%H:%M')
                    out_time = datetime.strptime(data.get("out-time", "00:00"), '%H:%M')
                    working_hours += (out_time - in_time).total_seconds() / 3600

            return working_hours
        else:
            os.system('cls')
            print("Error: No attendance records found for the employee.")
            return 0



    def save_attendance_data(self):
        """ Save attendance data into a salary database file
        args: None
        return: None 
        """
        with open("attendance_record.json", "w") as file:
            json.dump(self.attendance_data, file)

    def __main__(self):
        os.system('cls')

        try:
            while True:
                print("Options:")
                print("1. Record Entry Time")
                print("2. Record Exit Time")
                print("3. Calculate Total Working Hours")
                print("4. Exit\n")

                option = input("Enter your choice (1/2/3/4): ")

                if option == '1':
                    employee_id = input("Enter employee ID: ")
                    entry_date = input("Enter entry date (dd-MM-YYYY): ")
                    in_time = input("Enter in-time (HH:MM 24-hour format): ")

                    if self.record_entry(employee_id, entry_date, in_time):
                        os.system('cls')
                        
                        print("Entry recorded successfully.")

                elif option == '2':
                    employee_id = input("Enter employee ID: ")
                    exit_date = input("Enter exit date (dd-MM-YYYY): ")
                    out_time = input("Enter out-time (HH:MM 24-hour format): ")

                    if self.record_exit(employee_id, exit_date, out_time):
                        os.system('cls')

                        print("Exit recorded successfully.")

                elif option == '3':
                    employee_id = input("Enter employee ID: ")
                    start_date = input("Enter start date (dd-MM-YYYY): ")
                    end_date = input("Enter end date (dd-MM-YYYY): ")

                    working_hours = self.calculate_working_hours(employee_id, start_date, end_date)
                    if working_hours is not None:
                        os.system('cls')
                        print(f"Total working hours for the employee: {working_hours:.2f} hours")

                elif option == '4':
                    os.system('cls')
                    print("Exiting...")
                    break
                else:
                    os.system('cls')
                    print("Invalid option. Please select a valid option.")
        except ValueError as e:
            print(f"Error: {e}")
            print("Exiting...")


# if __name__ == "__main__":
#     attendance = Attendance("employee_database.json", "attendance_record.json")
#     attendance.__main__()

