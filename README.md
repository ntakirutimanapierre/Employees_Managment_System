# Employee-Management-System

            INTRODUCTION
            
Welcome to this employee management system. This system helps an organisation to manage their employees. The system helps in solving many tasks. 
By using this information the HR manager can do employee management, track the attendance employees, deal with employee salaries and produce a some reports. The information such as employee in an organisation and their information attendance records, salary information are stored in json files. payslips are also generated as txt file which are stored in our system. 

            0. HOW DOES IT WORK?
This is the first functionality to be used by the HR manager. To manage the employee, the HR will run the tester file and follow this procedures.

1. Run the sytem: run the tester class to start the system or you can run the file called HRMISRUNQ.bat if you have anaconda installed. 
2. Select 1 for the employee management functionality
3. Select 2 to run the attendance functionality
4. Select 3 to run salary calculation and salary reports
4. If you want to exit the system select 4

If you select any key, the sytem will give you a message and rerun, it will again give you option to select the functionality you want to perform. Let us explore how each functionality work.

            1. EMPLOYEE MANAGEMENT
This functionality will give the HR manager a chance to add employees, remove employee, view the employees information and update employee details. 
            1.1 ADD EMPLOYEE
To enter an employee, we expect the HR manager to understand the type employee she/he is going to add (Inter, Manager or Directors). Selecting the type, the system will generate a unique employee id and ask you for this employee attributes (names, salary) and then create a unique company email using the name of the company. It will the ask for each job level specific attribues and create that employee object and then save that employee into employees' database. 

            1.2 REMOVE THE EMPLOYEE
To remove an employee, the HR manager will need to select the second option and put the unique employee id. Deleting a user from employee database, he will be automaticaly removed from payroll(if he was there) and from attendance database if he was there.

            1.3 VIEW EMPLOEYEE
This function will help the HR manager view the table containing of all employees in an organisation. To run it, select 3.

            1.4 UPDATE EMPLOYEE
This function will help the HR manager to select the unique ID of an employee and update the content of that person. So far, the system can help to change some basic information about employees but we expect to add more feature so as to update the job level in case the employee step up or step down. 

            2. ATTENDANCE TRACKING
The second option of the system is to track the attendance of each employees. This option has two main functionalities, one is to record attendance another VIEW ATTENDANCE SUMMARY.

            2.1 RECORD ATTENDANCE
The functionality to record attendance works manually, when user reachs at the organisation, the date and time-in will be recorded. The user will have to enter his id, the date and the system will ask for time in. if the id entered is not in the employees database that is to mean that it is wrong id, for there will be no existing employee with the entered id. In this case, the appropriate error message will be displayed. If the user wants to record timeout, the HR will have to put the exact date that he went in and manually record timeout. The data will be saved in attendance database. If the user did not add time in and now she want to record timeout the system will return error message. in fact, the date added while recording out-time should be already in the file for the input record.  

            2.2 VIEW ATTENDANCE SUMMARY
This function will help the HR manager to view the attendance summary of employees. The attendance summary id defined as the number of hours that a particular employee has worked during a certain period of time. The HR manager will be given a choice to view the summary of all employee of one employee. For both actions the HR manager will input the duration(respect the suggested format), and the system will display the information on screen in a tabular format.

            3. SALARY CALCULATION & REPORTING
Enable the HR manager to calculate the salary information of the employee for a the current month or for future period, view salary summary(report) for particular month or generate the payslips of all employee in payroll. 

            3.1 SALARY CALCULATION
The HR manager will be asked to provide the employee id of any employee and his/her salary will be calculated according to his or her job level as saved in employee database.
 - Every employee will get bonus of 1% of the base salary if the HR manager approves (added). 
 - Each employee will get the allowance of 5% of his her monthly base salary (added)
 - Each employee will pay tax of 30% of the base salary, and it will be paid in monthly installments (added)

FOR INTERNS:
    - The monthly base salary is calculated by taking annual base salary and times the intership durartion in months over 12.

FOR MANAGERS:
    - In addition to their monthly salary that is calculated like other employees, they get more earning of a rate between 0 and 60 percent of the annual base salary.

FOR DIRECTORS:
    - In addition to the payment of base salary, they receive annual bonus and they receive these money on a equal monthly installments.

The calculated salary is added on salary database, the json file,  that was refered to in the the above sections as payroll.

            3.2 VIEW SALARY SUMMARY
This functionality allow the HR manager to view the summary of the employee payment history for a given month. The HR can choose to view the information for a specific employee by providing his employee ID or choose to view the payment summary for all empoyee in that given month. The function will return the salary history for that month for the entire period this employee was in the company salary database.

            3.3 GENERATE PAYSLIP
This functionality will help the HR manager to generate the payslip of each employee in the payroll for the last payroll that the salary was calculated. The payslip will be a text file that contains the employee information including the JOB LEVEL and the total deduction made from that employee. The next time the HR will run this function, the payslips will be replaced with all data. The challenge here is that the system will allow the user generate payslips for employee that was selected in the far past if there is not updated info. We are trying to handle it.


            UNIT TESTS
we designed three testers for the checking the functioning our classes.
The first one is for attendance class which verify the entered in-time, and in-time and provide the test results whether the entered time in or/and entry date is correct or not.The second one is for salary class which verify how calculation are being done, the correctness of the calculations and issue the appropriate test results. we added examples to test whether our testers are really working appropriately. The third tester is for HRMIS class which oversees the management of employee that is whether adding or removing employee in the database has been completed successfully. The reason why we chose to implement testers for above classes,  is that those classes have functionalities which are more likely to trigger problems within the system. 
In addition, some of those testers return test failure  and others return test success as approriate.

         4. LAST WORDS # futute improvement
The interface was created to run the system but we are also looking forward to creating a login crendentials such that the system can be accessed only by authorised HR people for ensuring security.
