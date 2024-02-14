import unittest
import json
import os
from Attendance import Attendance

class TestAttendance(unittest.TestCase):
    def setUp(self):
        # Create a temporary employee database file
        self.employee_db_file = "temp_employee_db.json"
        with open(self.employee_db_file, "w") as file:
            employee_data = {
                "employee1": {
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "john.doe@example.com"
                },
                "employee2": {
                    "first_name": "Jane",
                    "last_name": "Smith",
                    "email": "jane.smith@example.com"
                }
            }
            json.dump(employee_data, file)

        # Create a separate test attendance record file
        self.attendance_file = "test_attendance.json"
        with open(self.attendance_file, "w") as file:
            attendance_data = {}
            json.dump(attendance_data, file)

        # Initialize the Attendance object with the temporary files
        self.attendance = Attendance(self.employee_db_file, self.attendance_file)

    def tearDown(self):
        # Clean up the test attendance file
        os.remove(self.attendance_file)

    def test_record_entry(self):
        # Test recording entry
        entry_date = "2023-11-01"
        in_time = "09:00"
        self.assertTrue(self.attendance.record_entry("employee1", entry_date, in_time))

        # Test recording entry with invalid employee ID
        self.assertFalse(self.attendance.record_entry("nonexistent_employee", entry_date, in_time))

        # Test recording entry with invalid date
        invalid_date = "2023-13-01"  # Invalid month
        self.assertFalse(self.attendance.record_entry("employee2", invalid_date, in_time))

        # Test recording entry with invalid time
        invalid_time = "25:00"  # Invalid hour
        self.assertFalse(self.attendance.record_entry("employee1", entry_date, invalid_time))

    def test_entry_time(self):
        # Test entry time format
        entry_date = "2023-11-01"
        valid_time = "09:00"
        invalid_time = "09:00"  # Invalid format
        self.assertTrue(self.attendance.record_entry("employee1", entry_date, valid_time))
        self.assertFalse(self.attendance.record_entry("employee1", entry_date, invalid_time))

def main():
    while True:
        print("Main Menu:")
        print("1. Test record_entry")
        print("2. Test entry_time")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            unittest.main(defaultTest="TestAttendance.test_record_entry")
        elif choice == "2":
            unittest.main(defaultTest="TestAttendance.test_entry_time")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
