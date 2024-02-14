# Run the whole HRMS class here
from HRMIS import HRMIS
if __name__ == "__main__":
    HRMS = HRMIS('employee_database.json', 'attendance_record.json', 'salary_data.json')            
    HRMS.__main__()