import unittest
import json
import os
from Salary import Salary

class TestSalary(unittest.TestCase):
    def setUp(self):
        # Create a temporary employee database file that we will use for testing the database
        self.employee_db_file = "temp_employee_db.json"
        with open(self.employee_db_file, "w") as file:
            employee_data = {
                "employee1": {
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "john.doe@example.com",
                    "Job Level": "Intern",
                    "base salary": 2000
                },
                "employee2": {
                    "first_name": "Jane",
                    "last_name": "Smith",
                    "email": "jane.smith@example.com",
                    "Job Level": "Manager",
                    "base salary": 3000
                }
            }
            json.dump(employee_data, file)

        # Create a separate test salary data file
        self.salary_data_file = "test_salary_data.json"
        with open(self.salary_data_file, "w") as file:
            salary_data = {}
            json.dump(salary_data, file)

        # Initialize the Salary object with the temporary files and an employee ID
        self.salary = Salary(self.employee_db_file, self.salary_data_file, "employee1")

    def tearDown(self):
        # Clean up the test files
        os.remove(self.employee_db_file)
        os.remove(self.salary_data_file)

    def test_calculate_salary_per_employee_type(self):
        # Test calculating salary for Intern
        salary = self.salary.calculate_salary_per_employee_type()
        self.assertEqual(salary, 2000)  # Salary for Intern should be base salary

    def test_allowance(self):
        allowance = self.salary.allowance()
        self.assertEqual(allowance, 8.33)  # 5% of 2000

    def test_tax(self):
        tax = self.salary.tax()
        self.assertEqual(tax, 50.0)  # 30% of 2000 / 12

    def test_bonus(self):
        bonus = self.salary.bonus(check=True)
        self.assertEqual(bonus, 1.67)  # 1% of 2000 / 12

    def test_net_salary(self):
        net_salary = self.salary.net_salary()
        self.assertEqual(net_salary, 1959.0)  # Base salary (2000) - Tax (50) + Bonus (1.67)

    def test_save_salary_data(self):
        self.salary.save_salary_data()

        # Load the salary data file and check if data is saved
        with open(self.salary_data_file, "r") as file:
            salary_data = json.load(file)
            self.assertTrue("employee1" in salary_data)

def main():
    while True:
        print("Main Menu:")
        print("1. Test calculate_salary_per_employee_type")
        print("2. Test allowance")
        print("3. Test tax")
        print("4. Test bonus")
        print("5. Test net_salary")
        print("6. Test save_salary_data")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            unittest.main(defaultTest="TestSalary.test_calculate_salary_per_employee_type")
        elif choice == "2":
            unittest.main(defaultTest="TestSalary.test_allowance")
        elif choice == "3":
            unittest.main(defaultTest="TestSalary.test_tax")
        elif choice == "4":
            unittest.main(defaultTest="TestSalary.test_bonus")
        elif choice == "5":
            unittest.main(defaultTest="TestSalary.test_net_salary")
        elif choice == "6":
            unittest.main(defaultTest="TestSalary.test_save_salary_data")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
