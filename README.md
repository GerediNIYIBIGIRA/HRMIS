# HRMIS - Human Resources Management Information System

The HRMIS is a Python-based system designed for managing employee information, attendance records, and payroll calculations. It's tailored to provide a user-friendly interface for HR professionals, streamlining the management of employee data and HR-related tasks.

## Usage Guide

### Step 1: Launch the HRMIS

1.  **Prerequisites:** Ensure you have Python 3.x installed on your computer.
2.  **Setup:**
    -   Download the HRMIS code to your local machine.
    -   Open your preferred Python environment (e.g., VS Code, PyCharm, Jupyter Notebook) and navigate to the directory where the HRMIS code is located.
    -   Run the system.

### Step 2: Main Menu

Upon executing the HRMIS, you'll encounter the main menu presenting the following options:
HRMIS Menu:
1. Add Employee
2. Update Employee
3. Remove Employee
4. Generate Employee List
5. Record Attendance
6. Generate Attendance Summary
7. Generate Salary Summary
8. Save Data to File
9. Load Data from File
10. Exit
### Step 3: Add Employee (Option 1)

1.  Choose option 1 to add a new employee to the system.
2.  Provide the necessary employee information like Employee ID, First Name, Last Name, Email, Salary, and select the Employee Type (Intern, Manager, or Director).
3.  Based on the employee type, additional details might be required, such as University Name, Program Name, Internship Duration, Department, Number of Direct Reports, Management Allowance Rate, or Annual Bonus.
4.  The system ensures the uniqueness of the Employee ID.

### Step 4: Update Employee (Option 2)

1.  Select option 2 to update an existing employee's information.
2.  Enter the Employee ID you want to update.
3.  Specify the number of fields you wish to update and provide the field name and new value for each field, enabling modification of details like First Name, Last Name, Email, and Salary.

### Step 5: Remove Employee (Option 3)

1.  Opt for option 3 to remove an employee from the system.
2.  Enter the Employee ID of the employee you wish to remove.

### Step 6: Generate Employee List (Option 4)

1.  Select option 4 to generate a list of all employees in the system.
2.  The list includes Employee ID, Full Name, Email, Salary, and Employee Type.

### Step 7: Record Attendance (Option 5)

1.  Choose option 5 to record attendance for an employee.
2.  Enter the Employee ID for the employee's attendance record.
3.  Provide the Date (in the format YYYY-MM-DD), In-Time (in the format HH:MM), and Out-Time (in the format HH:MM).
4.  The system validates the date and time formats.

### Step 8: Generate Attendance Summary (Option 6)

1.  Select option 6 to generate an attendance summary for a specific employee.
2.  Provide the Employee ID for the employee whose attendance summary you wish to view.
3.  The system displays the date, in-time, and out-time for each attendance record.

### Step 9: Generate Salary Summary (Option 7)

1.  Choose option 7 to calculate the monthly salary for an employee.
2.  Enter the Employee ID and details including Base Salary, Allowances, and Bonuses.
3.  The system computes the total monthly salary, accounting for an 18% deduction from the base salary.

### Step 10: Save Data to File (Option 8)

1.  Opt for option 8 to store all HRMIS data, encompassing employee information and attendance records, in a JSON file named "hrmis_data.json."
2.  Ensure to perform this operation after each data manipulation to reflect the changes in the files.

### Step 11: Load Data from File (Option 9)

1.  Choose option 9 to load HRMIS data from the "hrmis_data.json" file, allowing you to resume work with previously saved data.
2.  Remember to load data before manipulating the system's information.

### Step 12: Exit (Option 10)

1.  Select option 10 to exit the HRMIS system.

## Working Principles and Class Descriptions

### Classes Overview

#### Employee Class

-   Serves as the base class for different employee types.
-   Stores common attributes like employee ID, first name, last name, email, position, and salary.
-   Employees have methods to display their details and calculate earnings.

#### Intern, Manager, Director Classes

-   Subclasses of the Employee class representing different employee types (Intern, Manager, Director).
-   Each class has specific attributes and overrides the calculate_earnings method for customized earnings calculation.

#### Attendance Class

-   Manages attendance records for employees.
-   Allows recording and displaying employee attendance records.

#### PaySlip Class

-   Generates pay slips for employees.
-   Takes employee ID and total salary to produce a pay slip saved in a text file.

#### HRMIS Class

-   Acts as the primary HRMIS system.
-   Stores employee data, attendance records, and provides functions to manage employees and data.
-   Contains methods to add, update, remove employees, record attendance, generate reports, and save/load data to/from files.

### System Usage and Overview

The guide details the various functionalities and operations within the HRMIS system, facilitating HR professionals in managing employee data, attendance, payroll, and file management. Users can efficiently add, update, remove employees, record attendance, calculate salaries, and save/load data to/from files, enabling seamless HR operations and data management.

Ensure to run `save_data_to_file()` after each action to reflect the changes in the data files. Additionally, loading data before making any data manipulations is essential to maintain data consistency.
## Class: Employee

**Description:** This class represents an Employee in the HRMIS (Human Resource Management Information System).

### Methods

#### `__init__(self, employee_id, first_name, last_name, position, email, salary)`

**Description:** Initializes an instance of an Employee.

**Parameters:**
- `employee_id` (int): Unique identifier for the employee.
- `first_name` (str): First name of the employee.
- `last_name` (str): Last name of the employee.
- `position` (str): Position or role of the employee.
- `email` (str): Email address of the employee.
- `salary` (float): Annual salary of the employee.

#### `display_info(self)`

**Description:** Displays information of the employee.

**Usage Example:**
```python
employee = Employee(101, "John", "Doe", "Manager", "john@example.com", 60000.0)
employee.display_info()#### `  
calculate_earnings(self)
```
**Description:** Calculates the earnings for the employee.

**Return:** Earnings of the employee (float).

**Usage Example:**
```python
employee = Employee(101, "John", "Doe", "Manager", "john@example.com", 60000.0) earnings = employee.calculate_earnings()
```
## Class: Intern (Derived from Employee)

**Description:** This class represents an Intern in the HRMIS.

### Methods

#### `__init__(self, employee_id, first_name, last_name, position, email, salary, university_name, program_name, internship_duration)`

**Description:** Initializes an instance of an Intern.

**Parameters:**

-   Similar to `Employee` with additional:
    -   `university_name` (str): Name of the university the intern is associated with.
    -   `program_name` (str): Name of the program.
    -   `internship_duration` (int): Duration of the internship (in months).

#### `calculate_earnings(self)`

**Description:** Calculates the earnings for the intern based on the internship duration.

**Return:** Earnings of the intern (float).

## Class: Manager (Derived from Employee)

**Description:** This class represents a Manager in the HRMIS.

### Methods

#### `__init__(self, employee_id, first_name, last_name, position, email, salary, department, num_direct_reports, management_allowance_rate)`

**Description:** Initializes an instance of a Manager.

**Parameters:**

-   Similar to `Employee` with additional:
    -   `department` (str): Department in which the manager works.
    -   `num_direct_reports` (int): Number of employees directly managed by the manager.
    -   `management_allowance_rate` (float): Rate of management allowance (as a percentage).

#### `calculate_earnings(self)`

**Description:** Calculates the earnings for the manager, including management allowance.

**Return:** Earnings of the manager (float).

## Class: Director (Derived from Employee)

**Description:** This class represents a Director in the HRMIS.

### Methods

#### `__init__(self, employee_id, first_name, last_name, position, email, salary, department, annual_bonus)`

**Description:** Initializes an instance of a Director.

**Parameters:**

-   Similar to `Employee` with additional:
    -   `department` (str): Department in which the director works.
    -   `annual_bonus` (float): Annual bonus received by the director.

#### `calculate_earnings(self)`

**Description:** Calculates the earnings for the director, including the annual bonus.

**Return:** Earnings of the director (float).

## Class: Attendance

**Description:** This class manages employee attendance records in the HRMIS.

### Methods

#### `__init__(self)`

**Description:** Initializes an instance of the Attendance class.

#### `record_attendance(self, employee_id, date, in_time, out_time)`

**Description:** Records employee attendance.

**Parameters:**

-   `employee_id` (int): ID of the employee for whom attendance is recorded.
-   `date` (str): Date of the attendance record (in "YYYY-MM-DD" format).
-   `in_time` (str): Time of arrival (in "HH:MM" format).
-   `out_time` (str): Time of departure (in "HH:MM" format).

#### `display_attendance(self, employee_id)`

**Description:** Displays attendance records of a specific employee.

**Parameters:**

-   `employee_id` (int): ID of the employee.

#### `display_attendance_all_employees(self, hrmis)`

**Description:** Displays attendance records of all employees.

**Parameters:**

-   `hrmis` (HRMIS instance): The HRMIS system used to access employee data.

## Class: PaySlip

**Description:** This class generates pay slips for employees in the HRMIS.

### Methods

#### `generate_pay_slip(self, employee_id, total_salary)`

**Description:** Generates a pay slip for an employee and saves it in a text file.

**Parameters:**

-   `employee_id` (int): ID of the employee for whom the pay slip is generated.
-   `total_salary` (float): Total monthly salary of the employee.

## Class: HRMIS

**Description:** This class manages employee data, attendance, and pay slip generation in the HRMIS.

### Methods

#### `__init__(self)`

**Description:** Initializes an instance of the HRMIS class.

#### `add_employee(self, employee)`

**Description:** Adds an employee to the HRMIS.

**Parameters:**

-   `employee` (Employee instance): The employee to be added.

#### `update_employee(self, employee_id, updated_employee_data)`

**Description:** Updates employee information.

**Parameters:**

-   `employee_id` (int): ID of the employee to be updated.
-   `updated_employee_data` (dict): Dictionary containing updated employee information.

#### `remove_employee(self, employee_id)`

**Description:** Removes an employee from the HRMIS.

**Parameters:**

-   `employee_id` (int): ID of the employee to be removed.

#### `generate_employee_list(self)`

**Description:** Generates a list of all employees and displays their information.

#### `record_attendance(self, employee_id, date, in_time, out_time)`

**Description:** Records employee attendance.

**Parameters:**

-   `employee_id` (int): ID of the employee for whom attendance is recorded.
-   `date` (str): Date of the attendance record (in "YYYY-MM-DD" format).
-   `in_time` (str): Time of arrival (in "HH:MM" format).
-   `out_time` (str): Time of departure (in "HH:MM" format).

#### `display_attendance(self, employee_id)`

**Description:** Displays attendance records of a specific employee.

**Parameters:**

-   `employee_id` (int): ID of the employee.

#### `display_attendance_all_employees(self, hrmis)`

**Description:** Displays attendance records of all employees.


**Parameters:**

-   `hrmis` (HRMIS instance): The HRMIS system used to access employee data.

#### `calculate_monthly_salary(self, employee_id)`

**Description:** Calculates the monthly salary for an employee.

**Parameters:**

-   `employee_id` (int): ID of the employee.

#### `generate_monthly_salary_report(self, hrmis)`

**Description:** Generates a monthly salary report for all employees.

**Parameters:**

-   `hrmis` (HRMIS instance): The HRMIS system used to access employee data.

#### `save_data_to_file(self)`

**Description:** Saves HRMIS data to a JSON file.

#### `load_data_from_file(self)`

**Description:** Loads HRMIS data from a JSON file.

## Employee Salary Calculation

### Intern
The salary for an Intern is determined based on their provided salary and the duration of their internship:
```python
internship_duration = getattr(employee, "internship_duration")
monthly_base_salary = round(base_salary / internship_duration, 2)
monthly_taxes = round(monthly_base_salary * 18 / 100, 2)
monthly_salary = monthly_base_salary - monthly_taxes
```
-   **Internship Full Salary:** Total salary provided for the internship duration.
-   **Duration:** The length of the internship in months.
-   **Gross Salary (monthly):** Calculated from the total salary divided by the internship duration.
-   **Taxes (monthly):** 18% deduction from the gross monthly salary.
-   **Calculated Monthly Salary:** Monthly salary after deducting taxes.

### Manager

For Managers, the salary calculation includes the base salary, management allowance rate, taxes, social security savings, and other allowances:
```python
management_allowance_rate = getattr(employee, "management_allowance_rate")
monthly_base_salary = round(base_salary / 12, 2)
monthly_taxes = round(monthly_base_salary * 18 / 100, 2)
social_security_savings = round(monthly_base_salary * 12 / 100, 2)
allowances = round(monthly_base_salary * management_allowance_rate, 2)
monthly_salary = monthly_base_salary + allowances - monthly_taxes - social_security_savings
```
-   **Annual Salary:** Total salary for the year.
-   **Monthly Base Salary:** Monthly salary calculated from the annual salary.
-   **Monthly Allowances:** Additional allowance based on the provided rate.
-   **Monthly Taxes:** 18% deduction from the monthly salary.
-   **Social Security Savings:** 12% for social security savings and insurance.
-   **Calculated Monthly Salary:** Final monthly salary after considering all deductions and allowances.

### Director

The salary calculation for Directors involves the base salary, annual bonus, taxes, social security savings, and monthly bonus:
```python
annual_bonus = getattr(employee, "annual_bonus")
monthly_bonus = round(annual_bonus / 12, 2)
monthly_base_salary = round(base_salary / 12, 2)
monthly_taxes = round(monthly_base_salary * 18 / 100, 2)
social_security_savings = round(monthly_base_salary * 12 / 100, 2)
monthly_salary = monthly_base_salary + monthly_bonus - monthly_taxes - social_security_savings
```
-   **Annual Salary:** Total salary for the year, including base salary and annual bonus.
-   **Monthly Base Salary:** Monthly salary derived from the total annual salary.
-   **Monthly Bonuses:** Monthly bonus calculated from the annual bonus.
-   **Monthly Taxes:** 18% deduction from the monthly salary.
-   **Social Security Savings:** 12% for social security savings and insurance.
-   **Calculated Monthly Salary:** Final monthly salary considering bonuses and deductions.

The `calculate_monthly_salary()` method in the HRMIS system triggers the salary calculation based on the employee's type and relevant attributes. After computing the salary, a pay slip is generated for the employee.