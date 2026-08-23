#scenario no.2

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def get_category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def display(self):
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Salary      : Rs.", self.salary)
        print("Category    :", self.get_category())
        print("--------------------------------")


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_all(self):
        print("\n========== EMPLOYEE DETAILS ==========")

        for employee in self.employees:
            employee.display()


# Main Program
company = Company()

e1 = Employee(101, "pari", 80000)
e2 = Employee(102, "Priya", 55000)
e3 = Employee(103, "Aman", 30000)

company.add_employee(e1)
company.add_employee(e2)
company.add_employee(e3)

company.display_all()

#output
'''========== EMPLOYEE DETAILS ==========

Employee ID : 101
Name        : pari
Salary      : Rs. 80000
Category    : High Salary
--------------------------------
Employee ID : 102
Name        : Priya
Salary      : Rs. 55000
Category    : Medium Salary
--------------------------------
Employee ID : 103
Name        : Aman
Salary      : Rs. 30000
Category    : Low Salary
--------------------------------'''



#scenario no.5

class Patient:
    def __init__(self, patient_id, name, treatment_cost):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost

    def get_category(self):
        if self.treatment_cost >= 50000:
            return "Special"
        else:
            return "General"

    def display(self):
        print("Patient ID     :", self.patient_id)
        print("Name           :", self.name)
        print("Treatment Cost : Rs.", self.treatment_cost)
        print("Category       :", self.get_category())
        print("--------------------------------")


class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_all(self):
        print("\n========== HOSPITAL PATIENT RECORDS ==========")

        for patient in self.patients:
            patient.display()


# Main Program
hospital = Hospital()

p1 = Patient(101, "Riya", 75000)
p2 = Patient(102, "Pari", 30000)
p3 = Patient(103, "Bhumi", 60000)

hospital.add_patient(p1)
hospital.add_patient(p2)
hospital.add_patient(p3)

hospital.display_all()


#output
'''========== HOSPITAL PATIENT RECORDS ==========

Patient ID     : 101
Name           : Riya
Treatment Cost : Rs. 75000
Category       : Special
--------------------------------
Patient ID     : 102
Name           : Pari
Treatment Cost : Rs. 30000
Category       : General
--------------------------------
Patient ID     : 103
Name           : Bhumi
Treatment Cost : Rs. 60000
Category       : Special
--------------------------------'''