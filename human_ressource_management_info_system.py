import json
from datetime import datetime

class Employee:
    def __init__(self, employee_id, first_name, last_name, position, email, salary):
        # Initialize employee attributes
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.position = position
        self.salary = salary

    def display_info(self):
        # Display employee information
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Salary: ${self.salary}")
        print(f"Position: {self.position}")

    def calculate_earnings(self):
        # Calculate earnings for the employee
        return self.salary

# Intern class derived from Employee
class Intern(Employee):
    def __init__(self, employee_id, first_name, last_name, position, email, salary, university_name, program_name, internship_duration):
        # Call the constructor of the base class (Employee)
        super().__init__(employee_id, first_name, last_name, position, email, salary)
        # Initialize intern-specific attributes
        self.university_name = university_name
        self.program_name = program_name
        self.internship_duration = internship_duration

    def calculate_earnings(self):
        # Calculate the earnings for an intern
        return (self.salary * self.internship_duration) / 12

# Manager class derived from Employee
class Manager(Employee):
    def __init__(self, employee_id, first_name, last_name, position, email, salary, department, num_direct_reports, management_allowance_rate):
        # Call the base class constructor
        super().__init__(employee_id, first_name, last_name, position, email, salary)
        # Initialize manager-specific attributes
        self.department = department
        self.num_direct_reports = num_direct_reports
        self.management_allowance_rate = management_allowance_rate / 100

    def calculate_earnings(self):
        # Calculate the earnings for a manager
        base_earnings = super().calculate_earnings()
        management_allowance = base_earnings * self.management_allowance_rate
        return base_earnings + management_allowance

# Director class derived from Employee
class Director(Employee):
    def __init__(self, employee_id, first_name, last_name, position, email, salary, department, annual_bonus):
        # Call the base class constructor
        super().__init__(employee_id, first_name, last_name, position, email, salary)
        # Initialize director-specific attributes
        self.department = department
        self.annual_bonus = annual_bonus

    def calculate_earnings(self):
        # Calculate the earnings for a director
        base_earnings = super().calculate_earnings()
        return base_earnings + self.annual_bonus

# Attendance class to manage employee attendance records
class Attendance:
    def __init__(self):
        self.attendance_records = {}  # Store attendance records

    def record_attendance(self, employee_id, date, in_time, out_time):
        # Record employee attendance
        if employee_id not in self.attendance_records:
            self.attendance_records[employee_id] = []
        self.attendance_records[employee_id].append({
            "date": date,
            "in_time": in_time,
            "out_time": out_time
        })

    def display_attendance(self, employee_id):
        # Display attendance of a specific employee
        if employee_id in self.attendance_records:
            for record in self.attendance_records[employee_id]:
                print(f"Date: {record['date']}, In-Time: {record['in_time']}, Out-Time: {record['out_time']}")
        else:
            print("No attendance records found for this employee.")

    def display_attendance_all_employees(self, hrmis):
        # Display attendance records of all employees
        print("ATTENDANCE OF ALL EMPLOYEES")
        print(f"____________________________")
        counting = 0
        for employee_id, records in self.attendance_records.items():
            counting += 1
            employee = hrmis.employee_data.get(int(employee_id))
            if employee:
                print()
                print(f"Employee ID: {employee_id}")
                print(f"Name: {employee.first_name} {employee.last_name}")
                print(f"Recorded Attendance:")
                attendance_found = False  # Variable to track if attendance is found for this employee
                for record in records:
                    print(f"Date: {record['date']}, In-Time: {record['in_time']}, Out-Time: {record['out_time']}")
                    attendance_found = True  # Mark attendance as found
                if not attendance_found:
                    print("No attendance records to display yet")
            else:
                print(f"No employee found with ID: {employee_id}")

        if counting == 0:
            print("No attendance records to display yet")

# PaySlip class to generate pay slips for employees
class PaySlip:
    def generate_pay_slip(self, employee_id, total_salary):
        # Generate pay slip for an employee and save it in a file
        file_name = f"EMPLOYEE_{employee_id}.txt"
        with open(file_name, "w") as file:
            file.write(f"Employee ID: {employee_id}\n")
            file.write(f"Total Salary: ${total_salary:.2f}\n")
            print(f"Pay slip for Employee ID {employee_id} generated and saved as {file_name}")

# HRMIS class to manage employee data
class HRMIS:
    def __init__(self):
        self.employee_data = {}  # Store employee data
        self.attendance_system = Attendance()  # Initialize the attendance system
        self.pay_slip_generator = PaySlip()  # Initialize pay slip generator

    def add_employee(self, employee):
        if employee.employee_id in self.employee_data:
            raise Exception("Employee ID already exists. Please use a unique ID.")
        self.employee_data[employee.employee_id] = employee
    
    # A method for updating employee information
    def update_employee(self, employee_id, updated_employee_data):  
        if employee_id in self.employee_data:
            employee = self.employee_data[employee_id]
            for key, value in updated_employee_data.items():
                setattr(employee, key, value)
            print("Employee information updated.")
        else:
            print("Employee not found.")

    # A method to rempve delete employee
    def remove_employee(self, employee_id):
        if employee_id in self.employee_data:
            del self.employee_data[employee_id]
            print("Employee removed.")
        else:
            print("Employee not found.")

    # A method to generate employee list
    def generate_employee_list(self):
        print()
        print("ALL EMPLOYEES' INFORMATION:")
        print("__________________________")
        for employee in self.employee_data.values():
            print()
            employee.display_info()

    # A method for recording attendance of an employee
    def record_attendance(self, employee_id, date, in_time, out_time):
        if employee_id not in self.employee_data:
            print("Employee not found.")
        else:
            try:
                datetime.strptime(date, "%Y-%m-%d")
                datetime.strptime(in_time, "%H:%M")
                datetime.strptime(out_time, "%H:%M")
                self.attendance_system.record_attendance(employee_id, date, in_time, out_time)
                print("Attendance recorded.")
            except ValueError:
                print("Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time.")

    def display_attendance(self, employee_id):
        self.attendance_system.display_attendance(employee_id)

    def display_attendance_all_employees(self, hrmis):
        self.attendance_system.display_attendance_all_employees(hrmis)

    # A method to calculate mothly salary of an employee
    def calculate_monthly_salary(self, employee_id):
        if employee_id not in self.employee_data:
            print("Employee not found.")
        else:
            try:
                employee = self.employee_data[employee_id]

                if employee.position in ["intern", "manager", "director"]:
                    base_salary = float(employee.salary)
                    print()
                    print(f"Salary information of {employee.first_name} {employee.last_name}")
                    print(f"______________________________________")
                    print()

                    # Now if the employee is an intern
                    if employee.position == "intern": 
                        internship_duration = getattr(employee, "internship_duration")
                        monthly_base_salary = round(base_salary / internship_duration, 2)
                        monthly_taxes = round(monthly_base_salary * 18 / 100, 2)
                        monthly_salary = monthly_base_salary - monthly_taxes
                        # Print details
                        print(f"Internship Full Salary: ${base_salary}")
                        print(f"Duration : {internship_duration} Months")
                        print(f"Gross Salary (monthly): ${monthly_base_salary}")
                        print(f"Taxes (monthly): ${monthly_taxes}")
                        print(f"Calculated Monthly Salary: ${monthly_salary}")
                    
                    # Now if the employee is manager
                    elif employee.position == "manager":
                        management_allowance_rate = getattr(employee, "management_allowance_rate") #Getting management allowance rate
                        monthly_base_salary = round(base_salary / 12, 2)
                        monthly_taxes = round(monthly_base_salary * 18 / 100, 2)
                        social_security_savings = round(monthly_base_salary * 12 / 100, 2) # 12% for social security saving and insurance
                        allowances = round(monthly_base_salary * management_allowance_rate, 2) #Calculating allowances based on the saved allowance rate
                        monthly_salary = monthly_base_salary + allowances - monthly_taxes - social_security_savings
                        # Print details
                        print(f"Annual Salary: ${base_salary}")
                        print(f"Monthly Base Salary: ${monthly_base_salary}")
                        print(f"Monthly Allowances: ${allowances}")
                        print(f"Monthly Taxes: ${monthly_taxes}")
                        print(f"Social Security Savings: ${social_security_savings}")
                        print(f"Calculated Monthly Salary: ${monthly_salary}")

                    # Else for the employee who is the director
                    else: 
                        annual_bonus = getattr(employee, "annual_bonus")
                        monthly_bonus = round(annual_bonus / 12, 2)
                        monthly_base_salary = round(base_salary / 12, 2)
                        monthly_taxes = round(monthly_base_salary * 18 / 100, 2)
                        social_security_savings = round(monthly_base_salary * 12 / 100, 2) # 12% for social security saving and insurance
                        monthly_salary = monthly_base_salary + monthly_bonus - monthly_taxes - social_security_savings
                        # Print details
                        print(f"Annual Salary: ${base_salary}")
                        print(f"Monthly Base Salary: ${monthly_base_salary}")
                        print(f"Monthly Bonuses: ${monthly_bonus}")
                        print(f"Monthly Taxes: ${monthly_taxes}")
                        print(f"Social Security Savings: ${social_security_savings}")
                        print(f"Calculated Monthly Salary: ${monthly_salary}")
                    self.pay_slip_generator.generate_pay_slip(employee_id, monthly_salary)

                else:
                    print("Employee role not recognized.")
            except Exception as e:
                print(f"Error calculating salary: {e}")

    # A method to generate monthly salary report for all employees
    def generate_monthly_salary_report(self, hrmis):
        print("SALARY REPORT OF ALL EMPLOYEES")
        print(f"______________________________")
        
        for employee_id, employee in self.employee_data.items():
            print()
            print(f"Employee ID: {employee_id}")
            print(f"Name: {employee.first_name} {employee.last_name}")
            print("Salary Details:")
            
            try:
                if employee.position == "intern":
                    internship_duration = getattr(employee, "internship_duration")
                    base_salary = float(employee.salary)
                    monthly_base_salary = round(base_salary * internship_duration / 12, 2)
                    monthly_taxes = round(monthly_base_salary * 18 / 100, 2)
                    monthly_salary = monthly_base_salary - monthly_taxes
                    print(f"Internship Full Salary: ${base_salary}")
                    print(f"Calculated Monthly Salary: ${monthly_salary}")

                elif employee.position == "manager":
                    base_salary = float(employee.salary)
                    monthly_base_salary = round(base_salary / 12, 2)
                    monthly_taxes = round(monthly_base_salary * 18 / 100, 2)
                    social_security_savings = round(monthly_base_salary * 12 / 100, 2)
                    management_allowance_rate = getattr(employee, "management_allowance_rate")
                    allowances = round(monthly_base_salary * management_allowance_rate, 2)
                    monthly_salary = monthly_base_salary + allowances - monthly_taxes - social_security_savings
                    print(f"Annual Salary: ${base_salary}")
                    print(f"Calculated Monthly Salary: ${monthly_salary}")

                elif employee.position == "director":
                    base_salary = float(employee.salary)
                    annual_bonus = getattr(employee, "annual_bonus")
                    monthly_bonus = round(annual_bonus / 12, 2)
                    monthly_base_salary = round(base_salary / 12, 2)
                    monthly_taxes = round(monthly_base_salary * 18 / 100, 2)
                    social_security_savings = round(monthly_base_salary * 12 / 100, 2)
                    monthly_salary = monthly_base_salary + monthly_bonus - monthly_taxes - social_security_savings
                    print(f"Annual Salary: ${base_salary}")
                    print(f"Calculated Monthly Salary: ${monthly_salary}")

                self.pay_slip_generator.generate_pay_slip(employee_id, monthly_salary)
            except Exception as e:
                print(f"Error generating salary: {e}")

    # Now a new method to save data in the json file which is acting as our database
    def save_data_to_file(self):
        with open("hrmis_data.json", "w") as file:
            data = {
                "employee_data": {
                    employee_id: {
                        "employee_type": employee.__class__.__name__,  # Store the class name
                        "first_name": employee.first_name,
                        "last_name": employee.last_name,
                        "email": employee.email,
                        "salary": employee.salary,
                        "position": employee.position,
                        # Additional details for different employee types
                        "university_name": getattr(employee, "university_name", None),
                        "program_name": getattr(employee, "program_name", None),
                        "internship_duration": getattr(employee, "internship_duration", None),
                        "department": getattr(employee, "department", None),
                        "num_direct_reports": getattr(employee, "num_direct_reports", None),
                        "management_allowance_rate": getattr(employee, "management_allowance_rate", None),
                        "annual_bonus": getattr(employee, "annual_bonus", None)
                    } for employee_id, employee in self.employee_data.items()
                },
                "attendance_records": self.attendance_system.attendance_records
            }
            json.dump(data, file)
        print("Data saved to file.")

    # A method to load data from the file
    def load_data_from_file(self):
        try:
            with open("hrmis_data.json", "r") as file:
                data = json.load(file)
                self.employee_data = {}
                for employee_id, employee_info in data["employee_data"].items():
                    if employee_info["employee_type"] == "Intern":
                        employee = Intern(
                            int(employee_id),
                            employee_info["first_name"],
                            employee_info["last_name"],
                            employee_info["position"],
                            employee_info["email"],
                            employee_info["salary"],
                            employee_info["university_name"],
                            employee_info["program_name"],
                            employee_info["internship_duration"]
                        )
                    elif employee_info["employee_type"] == "Manager":
                        employee = Manager(
                            int(employee_id),
                            employee_info["first_name"],
                            employee_info["last_name"],
                            employee_info["email"],
                            employee_info["position"],
                            employee_info["salary"],
                            employee_info["department"],
                            employee_info["num_direct_reports"],
                            employee_info["management_allowance_rate"]
                        )
                    elif employee_info["employee_type"] == "Director":
                        employee = Director(
                            int(employee_id),
                            employee_info["first_name"],
                            employee_info["last_name"],
                            employee_info["position"],
                            employee_info["email"],
                            employee_info["salary"],
                            employee_info["department"],
                            employee_info["annual_bonus"]
                        )
                    else:
                        employee = Employee(
                            int(employee_id),
                            employee_info["first_name"],
                            employee_info["last_name"],
                            employee_info["position"],
                            employee_info["email"],
                            employee_info["salary"]
                        )
                    setattr(employee, "position", employee_info["position"])
                    self.employee_data[int(employee_id)] = employee
                self.attendance_system.attendance_records = data["attendance_records"]
            print("Data loaded from file.")
        except FileNotFoundError:
            print("Data file not found.")

def main():
    hrmis = HRMIS()

    # Displaying the Interface Menu
    while True:
        print("\nHRMIS Menu:")
        print("_____________")
        print()
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Remove Employee")
        print("4. Generate Employee List")
        print("5. Record Attendance")
        print("6. Attendance Reports")
        print("7. Salary Reports")
        print("8. Save Data to File")
        print("9. Load Data from File")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        # Choice 1 which is to add employees
        if choice == 1:
            try:
                employee_id = int(input("Enter Employee ID: "))
                if employee_id in hrmis.employee_data:
                    print("Employee ID already exists. Please use a unique ID.")
                    continue
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                email = input("Enter Email: ")
                position = input("Enter Employee Type (Intern/Manager/Director): ").lower()

                if position == "intern":
                    university_name = input("Enter University Name: ")
                    program_name = input("Enter Program Name: ")
                    internship_duration = int(input("Enter Internship Duration (in months): "))
                    salary = float(input("Enter Internship Annual Salary: "))
                    employee = Intern(
                        employee_id,
                        first_name,
                        last_name,
                        position,
                        email,
                        salary,
                        university_name,
                        program_name,
                        internship_duration
                    )
                elif position == "manager":
                    department = input("Enter Department: ")
                    num_direct_reports = int(input("Enter Number of Direct Reports: "))
                    salary = float(input("Enter Annual Salary: "))
                    management_allowance_rate = float(input("Enter Management Allowance Rate (%): "))
                    employee = Manager(
                        employee_id,
                        first_name,
                        last_name,
                        position,
                        email,
                        salary,
                        department,
                        num_direct_reports,
                        management_allowance_rate
                    )
                elif position == "director":
                    department = input("Enter Department: ")
                    salary = float(input("Enter Annual Salary: "))
                    annual_bonus = float(input("Enter Annual Bonus: "))
                    employee = Director(
                        employee_id,
                        first_name,
                        last_name,
                        position,
                        email,
                        salary,
                        department,
                        annual_bonus
                    )
                else:
                    # If the employee type is not recognized, default to the Employee 
                    employee = Employee(employee_id, first_name, last_name, position, email, salary)

                hrmis.add_employee(employee)
            except ValueError:
                print("Invalid input. Employee ID should be an integer, and Salary should be a number.")

        # THe second choice whic is to update employee's information
        elif choice == 2:
            employee_id = int(input("Enter Employee ID to update: "))
            updated_data = {}
            field_count = int(input("Enter the number of fields to update: "))
            for _ in range(field_count):
                field_name = (input("Enter field name (e.g., first_name, last_name): ")).lower()
                field_value = input(f"Enter new value for {field_name}: ")
                updated_data[field_name] = field_value
            hrmis.update_employee(employee_id, updated_data)

        # Now the third choice whic is to remove employee from the list
        elif choice == 3:
            employee_id = int(input("Enter Employee ID to remove: "))
            hrmis.remove_employee(employee_id)

        # Now the Fourth choice of generating the list of all employees
        elif choice == 4:
            hrmis.generate_employee_list()

        # Now the fifth option for recording the attendance of an employee
        elif choice == 5:
            employee_id = int(input("Enter Employee ID for attendance: "))
            date = input("Enter Date (YYYY-MM-DD): ")
            in_time = input("Enter In-Time (HH:MM): ")
            out_time = input("Enter Out-Time (HH:MM): ")
            hrmis.record_attendance(employee_id, date, in_time, out_time)

        # Now the sixth option of the Attendance Reports
        elif choice == 6:
            print()
            print("ATTENDANCE REPORTS MENU:")
            print("________________________")
            print()
            print("1. Report of one Employee")
            print("2. Report of all employees")
            print("0. Exit")
            second_choice = int(input("Enter your choice: "))

            # For this option, we show attendace of one employee
            if second_choice == 1:
                employee_id = input("Enter Employee ID for attendance summary: ")
                hrmis.display_attendance(employee_id)

            # For this option, we show attendance all employees
            elif second_choice == 2:
                hrmis.display_attendance_all_employees(hrmis)

            # and for this we exit
            elif second_choice == 0:
                print("Exiting....")
                break
            
            # When the user enter wrong input, we exit
            else:
                print("Wrong choice. /n Exiting....")
                break
        
        # THis is the option of Salary reports
        elif choice == 7:
            print()
            print("SALARY REPORTS MENU:")
            print("________________________")
            print()
            print("1. Report of one Employee")
            print("2. Report of all employees")
            print("0. Exit")
            second_choice = int(input("Enter your choice: "))

            # if the user chosses 1, we show salary for one employee
            if second_choice == 1:
                employee_id = int(input("Enter Employee ID for salary calculation: "))
                try:
                    hrmis.calculate_monthly_salary(employee_id)
                except ValueError:
                    print("Invalid input. Salary-related fields should be numbers.")
            
            # If the user choses 2, we show the monthly salary report of all employees
            elif second_choice == 2:
                hrmis.generate_monthly_salary_report(hrmis)

            # For the option 0, we exit the program
            elif second_choice == 0:
                print("Exiting....")
                break

            # For a wrong choice, we also exit the program
            else:
                print("Wrong choice. /n Exiting....")
                break
        
        # Choice for saving data to file
        elif choice == 8:
            hrmis.save_data_to_file()

        # Choice for loading data to file
        elif choice == 9:
            hrmis.load_data_from_file()

        # For this choice, we exit the program
        elif choice == 0:
            print("Exiting HRMIS.")
            break

if __name__ == "__main__":
    main()


#@Copyright Geredi NIYIBIGIRA

