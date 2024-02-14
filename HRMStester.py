import unittest
import json
import os
from HRMIS import HRMIS  # Import HRMIS class


import unittest
import json
import os
from HRMIS import HRMIS  # Import HRMIS class

class TestHRMIS(unittest.TestCase):

    def setUp(self):
        # Create temporary JSON files for testing
        self.employee_db_file = "temp_employee_database.json"
        self.attendance_db_file = "temp_attendance_database.json"
        self.salary_db_file = "temp_salary_database.json"

        with open(self.employee_db_file, "w") as f:
            json.dump({}, f)
        with open(self.attendance_db_file, "w") as f:
            json.dump({}, f)
        with open(self.salary_db_file, "w") as f:
            json.dump({}, f)

        self.hrmis = HRMIS(self.employee_db_file, self.attendance_db_file, self.salary_db_file)

    def tearDown(self):
        # Delete temporary JSON files after testing
        os.remove(self.employee_db_file)
        os.remove(self.attendance_db_file)
        os.remove(self.salary_db_file)

    def test_email_generator(self):
        # Test the email generator method
        email = self.hrmis.email_generator(first_name = "John", last_name = "Doe")
        self.assertEqual(email, "john.doe@onepeople.org")

    def test_employee_id_generator(self):
        # Test the employee ID generator method
        employee_id = self.hrmis.employee_id_gerenerato()
        self.assertTrue(employee_id.startswith("CMU"))
        self.assertEqual(len(employee_id), 8)

    def test_add_employee(self):
        # Test the add_employee method
        self.hrmis.add_employee()
        # Add your assertions here based on how you expect the databases to

    def test_employee_id_generator(self):
        # Test the employee ID generator method
        employee_id = self.hrmis.employee_id_gerenerato()
        self.assertTrue(employee_id.startswith("CMU"))
        self.assertEqual(len(employee_id), 8)

    def test_update_employee(self):
        # Test the update_employee method
        # Assume that add_employee method should add an employee to the employee database
        self.hrmis.add_employee()
        with open("temp_employee_database.json", "r") as f:
            content = json.load(f)
        self.assertTrue(content)  # Check if the database is not empty

        employee_id = input("Enter the employee ID of the employee to update: ") #
        # Assume that update_employee method should update an employee in the employee database
        self.hrmis.update_employee(employee_id)
        with open("temp_employee_database.json", "r") as f:
            updated_content = json.load(f)
        self.assertNotEqual(content, updated_content)  # Check if the database has been updated

    def test_view_employee(self):
        # Test the view_employee method
        # Assume that add_employee method should add an employee to the employee database
        self.hrmis.add_employee()
        with open("temp_employee_database.json", "r") as f:
            content = json.load(f)
        self.assertTrue(content)  # Check if the database is not empty

        # Assume that view_employee method should return an employee from the employee database
        employee = self.hrmis.view_employee_list()
        self.assertIsNotNone(employee)  # Check if an employee is returned

    def test_remove_employee(self):
        # Test the remove_employee method
        # Assume that add_employee method should add an employee to the employee database
        self.hrmis.add_employee()
        with open("temp_employee_database.json", "r") as f:
            content = json.load(f)
        self.assertTrue(content)  # Check if the database is not empty

        emplyee_id = input("Enter the employee ID of the employee to remove: ")
        # Assume that remove_employee method should remove an employee from the employee database
        self.hrmis.remove_employee(emplyee_id)
        with open("temp_employee_database.json", "r") as f:
            updated_content = json.load(f)
        self.assertNotEqual(content, updated_content)  # Check if the database has been updated

    def test_generate_payslips(self):
        # Test the generate_payslips method
        self.hrmis.add_employee()
        with open("temp_salary_database.json", 'r') as f:
            content = json.load(f)

        # Assume that generate_payslips method should generate payslips for all employees in payroll
        employee_id = input("Enter the employee ID of the employee to calcuate salary: ")
        from Salary import Salary
        Salary = Salary("temp_employee_database.json", "temp_salary_database.json", employee_id)
        Salary.__main__()

        with open("temp_salary_database.json", 'r') as f:
            content = json.load(f)
            self.assertTrue(content)  # Check if the database is not empty
        object = content[employee_id]
        payslips = self.hrmis.generate_payslip(employee_id,object)
        self.assertIsNotNone(payslips)  # Check if payslips are generated

    def test_generate_salary_summary(self):
        # Test the generate_salary_summary method
        # Assume that add_employee method should add an employee to the employee database
        # self.hrmis.add_employee()

        with open("temp_employee_database.json", "r") as f:
            content = json.load(f)
        self.assertTrue(content)  # Check if the database is not empty

        # Assume that generate_salary_summary method should generate a salary summary for all employees in the employee database
        salary_summary = self.hrmis.view_salary_summary()
        self.assertIsNotNone(salary_summary)  # Check if a salary summary is generated

def main():
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    test_suite.addTest(test_loader.loadTestsFromTestCase(TestHRMIS))
    
    # Prompt the user for the test case to run
    print("Choose a task to run:")
    print("1. Test email generator")
    print("2. Test employee ID generator")
    print("3. Test add employee")
    print("4. Test update employee")
    print("5. Test view employee")
    print("6. Test remove employee")
    print("7. Test generate payslips")
    print("8. Test generate salary summary")

    choice = input("Enter the number of the task you want to run: ")

    if choice == "1":
        test_suite = unittest.TestSuite([TestHRMIS('test_email_generator')])
    elif choice == "2":
        test_suite = unittest.TestSuite([TestHRMIS('test_employee_id_generator')])
    elif choice == "3":
        test_suite = unittest.TestSuite([TestHRMIS('test_add_employee')])
    elif choice == "4":
        test_suite = unittest.TestSuite([TestHRMIS('test_update_employee')])
    elif choice == "5":
        test_suite = unittest.TestSuite([TestHRMIS('test_view_employee')])
    elif choice == "6":
        test_suite = unittest.TestSuite([TestHRMIS('test_remove_employee')])
    elif choice == "7":
        test_suite = unittest.TestSuite([TestHRMIS('test_generate_payslips')])
    elif choice == "8":
        test_suite = unittest.TestSuite([TestHRMIS('test_generate_salary_summary')])

    # Run the selected test
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_result = test_runner.run(test_suite)

    if test_result.wasSuccessful():
        print("Test passed.")
    else:
        print("Test failed.")

if __name__ == '__main__':
    main()

