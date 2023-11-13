import unittest
from datetime import datetime
from human_ressource_management_info_system import Employee, Intern, Manager, Director, Attendance, PaySlip, HRMIS

# import unittest
# from datetime import datetime

# Import your HRMIS classes here

class TestHRMIS(unittest.TestCase):
    def setUp(self):
        self.hrmis = HRMIS()

    def test_add_employee(self):
        employee = Employee(1, "Geredi", "NIYIBIGIRA", "Employee", "john@example.com", 50000)
        self.hrmis.add_employee(employee)
        self.assertEqual(len(self.hrmis.employee_data), 1)

    def test_update_employee(self):
        employee = Employee(1, "Geredi", "NIYIBIGIRA","Employee", "john@example.com", 50000)
        self.hrmis.add_employee(employee)
        updated_data = {"first_name": "Jane"}
        self.hrmis.update_employee(1, updated_data)
        self.assertEqual(self.hrmis.employee_data[1].first_name, "Jane")

    def test_remove_employee(self):
        employee = Employee(1, "Geredi", "NIYIBIGIRA", "Employee", "john@example.com", 50000)
        self.hrmis.add_employee(employee)
        self.hrmis.remove_employee(1)
        self.assertEqual(len(self.hrmis.employee_data), 0)

    def test_record_attendance(self):
        employee = Employee(1, "Geredi", "NIYIBIGIRA","Employee", "john@example.com", 50000)
        self.hrmis.add_employee(employee)
        self.hrmis.record_attendance(1, "2023-10-31", "09:00", "17:00")
        self.assertEqual(len(self.hrmis.attendance_system.attendance_records[1]), 1)

    def test_display_attendance(self):
        employee = Employee(1, "Geredi", "NIYIBIGIRA", "Employee", "john@example.com", 50000)
        self.hrmis.add_employee(employee)
        self.hrmis.record_attendance(1, "2023-10-31", "09:00", "17:00")
        self.assertEqual(self.hrmis.display_attendance(1), None)  # It should print attendance details.

    def test_generate_monthly_salary(self):
        employee = Employee(1, "Geredi", "NIYIBIGIRA", "Employee", "john@example.com", 60000)
        self.hrmis.add_employee(employee)
        self.hrmis.calculate_monthly_salary(1)
        # You can assert the generated pay slip contents here.

if __name__ == '__main__':
    unittest.main()