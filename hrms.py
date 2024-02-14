from Attendance import Attendance
from Salary import Salary
from datetime import datetime
import json
import os
import string
import random
from prettytable import PrettyTable
from Employee import Employee
from Intern import Intern
from Manager import Manager
from Director import Director
from Attendance import Attendance
from Salary import Salary


class HRMS:
    def __init__(self, employee_database, attendance_record, salary_record):
        self.__employee_database = employee_database
        self.__attendance_record = attendance_record
        self.__salary_record = salary_record
        os.system('cls')

    def email_generator(self, first_name, last_name, initial='', company='onepeople'):
        email = first_name + '.' + last_name + initial + '@' + company + '.org'
        return email.lower()

    def employee_id_generator(self, id_length=5, id_initial='CMU'):
        password_characters = string.ascii_uppercase + string.digits + string.ascii_lowercase
        password = ''.join(random.choice(password_characters) for _ in range(id_length))
        return id_initial + password

    def add_employee(self):
        os.system('cls')
        print('\nYou selected to add an employee you want to add\n1. Intern \n2. Manager \n3. Director \n4. Exit')
        choice = input('Enter your choice: ')

        while choice not in ['1', '2', '3', '4']:
            os.system('cls')
            print('Invalid choice: Try Again!\n')
            print('\n1. Intern \n2. Manager \n3. Director \n4. Exit')
            choice = input('Enter your choice: ')

        if choice == '4':
            os.system('cls')
            print('Exiting... Thank you for using HRMS\n')
            exit()

        employee_id = self.employee_id_generator()

        try:
            with open(self.__employee_database, "r") as f:
                content = json.load(f)

        except FileNotFoundError:
            os.system('cls')
            print("Employee database does not exist, we will create it")

        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')

        email = self.email_generator(first_name, last_name)

        for key, values in content.items():
            if values['email'] == email:
                os.system('cls')
                initial = self.employee_id_generator(id_length=1, id_initial='')
                email = self.email_generator(first_name, initial, last_name)
            else:
                pass

        os.system('cls')
        print(f'Email of {first_name} generated automatically: {email}')
        print(f'Employee Id of {first_name} is generated automatically: {employee_id}')

        base_salary = eval(input('Enter base salary: '))

        if choice == '1':
            university_name = input('You are going to add an intern: What is the intern university name: ')
            program_name = input('What is the intern program name: ')
            internership_duration = int(input('What is the internship duration (between 3 and 6): '))

            intern = Intern(
                employee_id,
                first_name,
                last_name,
                email,
                base_salary,
                university_name,
                program_name,
                0
            )

            intern.set_internership_duration(internership_duration)

            try:
                with open(self.__employee_database, "r") as f:
                    content = json.load(f)

                content[intern.get_employee_id()] = {
                    "first_name": intern.get_first_name(),
                    "last_name": intern.get_last_name(),
                    "email": intern.get_email,
                    "base salary": intern.get_base_salary,
                    "university name": intern.get_university_name(),
                    "program name": intern.get_program_name(),
                    "internership duration": intern.get_internership_duration(),
                    "Job Level": "Intern"
                }

                with open(self.__employee_database, "w") as f:
                    json.dump(content, f)

                os.system('cls')
                print("Employee added successfully")

            except FileNotFoundError:
                with open(self.__employee_database, "w") as f:
                    json.dump({intern.get_employee_id(): {
                        "first_name": intern.get_first_name(),
                        "last_name": intern.get_last_name(),
                        "email": intern.get_email,
                        "base salary": intern.get_base_salary,
                        "university name": intern.get_university_name(),
                        "program name": intern.get_program_name(),
                        "internership duration": intern.get_internership_duration(),
                        "Job Level": "Intern"
                    }}, f)

                os.system('clc')
                print("Employee added successfully")

        elif choice == '2':
            department_name = input('You are adding a Manager: What is the department name: ')
            number_of_direct_reports = int(input('How many direct reports: '))

            manager = Manager(
                employee_id,
                first_name,
                last_name,
                email,
                base_salary,
                department_name,
                number_of_direct_reports
            )

            try:
                with open(self.__employee_database, "r") as f:
                    content = json.load(f)

                content[manager.get_employee_id] = {
                    "first_name": manager.get_first_name,
                    "last_name": manager.get_last_name,
                    "email": manager.get_email,
                    "base salary": manager.get_base_salary,
                    "department name": manager.get_department_name,
                    "number of direct reports": manager.get_number_of_direct_reports,
                    "Job Level": "Manager"
                }

                with open(self.__employee_database, "w") as f:
                    json.dump(content, f)

                os.system('cls')
                print("Employee added successfully")

            except FileNotFoundError:
                with open(self.__employee_database, "w") as f:
                    json.dump({manager.get_employee_id: {
                        "first_name": manager.get_first_name,
                        "last_name": manager.get_last_name,
                        "email": manager.get_email,
                        "base salary": manager.get_base_salary,
                        "department name": manager.get_department_name(),
                        "number of direct reports": manager.get_number_of_direct_reports(),
                        "Job Level": "Manager"
                    }}, f)

                os.system('cls')
                print("Employee added successfully")

        elif choice == '3':
            department = input('Enter the department name: ')
            annual_bonus = eval(input('Enter the annual bonus: '))

            director = Director(
                employee_id,
                first_name,
                last_name,
                email,
                base_salary,
                department,
                annual_bonus
            )

            try:
                with open(self.__employee_database, "r") as f:
                    content = json.load(f)

                if employee_id in content:
                    os.system('cls')
                    print("Employee already exists")
                    return

                content[director.get_employee_id()] = {
                    "first_name": director.get_first_name(),
                    "last_name": director.get_last_name(),
                    "email": director.get_email,
                    "base salary": director.get_base_salary,
                    "department name": director.get_department,
                    "annual bonus": director.get_annual_bonus,
                    "Job Level": "Director"
                }

                with open(self.__employee_database, "w") as f:
                    json.dump(content, f)

                os.system('cls')
                print("Employee added successfully")

            except FileNotFoundError:
                with open(self.__employee_database, "w") as f:
                    json.dump({director.get_employee_id(): {
                        "first_name": director.get_first_name(),
                        "last_name": director.get_last_name(),
                        "email": director.get_email,
                        "base salary": director.get_base_salary,
                        "department name": director.get_department,
                        "annual bonus": director.get_annual_bonus,
                        "Job Level": "Director"
                    }}, f)

                os.system('cls')
                print("Employee added successfully")

        else:
            os.system('cls')
            print("Exiting... Thanks for using HRMS")
            exit()

    def remove_employee(self, employee_id):
        os.system('cls')

        try:
            with open(self.__employee_database, "r") as f:
                content = json.load(f)

            if employee_id in content:
                del content[str(employee_id)]

                with open(self.__employee_database, "w") as f:
                    json.dump(content, f)

                print(f"Employee '{employee_id}' removed successfully")

                try:
                    with open(self.attendance_file, "r") as f:
                        content = json.load(f)
                        del content[str(employee_id)]

                    with open(self.attendance_file, "w") as f:
                        json.dump(content, f)

                    print(f"Employee '{employee_id}' removed successfully on attendance database")

                except FileNotFoundError:
                    print("The attendance file not found")

                except KeyError:
                    print(f"Employee '{employee_id}' not found in attendance database")

                try:
                    with open(self.salary_file, "r") as f:
                        content = json.load(f)
                        del content[str(employee_id)]

                    with open(self.salary_file, "w") as f:
                        json.dump(content, f)

                    print(f"Employee '{employee_id}' removed successfully on salary database")

                except FileNotFoundError:
                    print("The salary data file not found")

                except KeyError:
                    print(f"Employee '{employee_id}' not found in our payroll")

            else:
                os.system('cls')
                print("Employee not found in our employee database, check with your HR")

        except FileNotFoundError:
            os.system('cls')
            print("Employee database file not found")

    def view_employee_list(self):
        os.system('cls')

        try:
            with open(self.__employee_database, "r") as f:
                content = json.load(f)

            table = PrettyTable()
            table.field_names = ["Employee ID", "First Name", "Last Name", "Email", "Job Level", "Base Salary"]

            for key, value in content.items():
                table.add_row([key, value['first_name'], value['last_name'], value['email'],
                               value['Job Level'], f"${float(value['base salary']):.2f}"])

            os.system('cls')
            print("Below is the table that shows our employees' information")
            print(table, '\n')

        except FileNotFoundError:
            os.system('cls')
            print("The employee database file not found")

    def update_employee(self, employee_id):
        os.system('cls')
        print('You selected to update employee: You cannot update Job Level!')

        try:
            with open(self.__employee_database, "r") as f:
                content = json.load(f)

            if employee_id not in content:
                os.system('cls')
                print(f"Employee '{employee_id}' not found")
                return

            choice = input('Do you want to change the first name (y/n)?: ')
            while choice not in ['y', 'n']:
                os.system('cls')
                print('Invalid choice')
                choice = input('Do you want to change the first name (y/n)?: ')

            if choice == 'y':
                content[employee_id]['first_name'] = input('Enter new first name: ')
            else:
                pass

            choice = input('Do you want to change the last name (y/n)?: ')
            while choice not in ['y', 'n']:
                os.system('cls')
                print('Invalid choice')
                choice = input('Do you want to change the last name (y/n)?: ')

            if choice == 'y':
                content[employee_id]['last_name'] = input('Enter new last name: ')
            else:
                pass

            choice = input('Do you want to change the base salary (y/n)?: ')
            while choice not in ['y', 'n']:
                os.system('cls')
                print('Invalid choice')
                choice = input('Do you want to change the base salary (y/n)?: ')

            if choice == 'y':
                content[employee_id]['base salary'] = input('Enter new base salary: ')
            else:
                pass

            choice = input('Do you want your email to be changed (y/n)?: ')
            while choice not in ['y', 'n']:
                os.system('cls')
                print('Invalid choice')
                choice = input('Do you want your email to be changed (y/n)?: ')

            if choice == 'y':
                email = self.email_generator(first_name=content[employee_id]['first_name'],
                                            last_name=content[employee_id]['last_name'])

                for key, values in content.items():
                    if values['email'] == email:
                        os.system('cls')
                        initial_characters = string.ascii_uppercase + string.digits + string.ascii_lowercase
                        initil = ''.join(random.choice(initial_characters) for _ in range(1))
                        email = self.email_generator(content[employee_id]['first_name'], initil, content[employee_id]['last_name'])
                    else:
                        pass

                content[employee_id]['email'] = email

            with open(self.__employee_database, "w") as f:
                json.dump(content, f)

            os.system('cls')
            print("Employee updated successfully")

        except FileNotFoundError:
            os.system('cls')
            print("The employee database file not found")

    def __main__(self):
        while True:
            choice = input('Enter your choice: ')

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.remove_employee(employee_id=input('Enter the employee id: '))
            elif choice == '3':
                self.view_employee_list()
            elif choice == '4':
                self.update_employee(employee_id=input('Enter the employee id: '))
            else:
                os.system('cls')
                print("Exiting... Thanks for using HRMS")
                exit()

Employees = "employee_database.json"
Attendance = "attendance_record.json"
employee_db_file = "employee_database.json"
salary_data_file = "salary_data.json"

HRMS = HRMS(Employees, Attendance, salary_data_file)

HRMS.__main__()













