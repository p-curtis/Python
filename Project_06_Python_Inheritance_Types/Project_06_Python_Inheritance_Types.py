import random

class Affiliate:
    def __init__(self, fullname):
        self.fullname = fullname

    def affiliate_print(self):
        print(f"\n{self.fullname}, you are an affiliate of Random School Name!")

class Student(Affiliate):
    def __init__(self, fullname, student_id):
        super().__init__(fullname)
        self.student_id = random.randint(000,200)
        
    def student_print(self):
        print(f"\nDatabase Details:\n{self.fullname} is a student.\nTheir Student ID # is: 2024-S-{self.student_id}.")

class Employee(Affiliate):
    def __init__(self, status):
        self.status = random.randint(0,1)
        if self.status == 0:
            self.status = "Inactive"
        elif self.status == 1:
            self.status = "Active"

    def employee_print(self):
        print(f"\nDatabase Details:\nEmployee: True.\nEmployment status is: {self.status}")

class Professor(Employee):
    def __init__(self, department):
        self.department = department

    def professor_print(self):
        print(f"Professor of department: {self.department}")

class Adjunct(Professor):
    def __init__(self, department, adjunct_status):
        super().__init__(department)
        self.adjunct_status = random.randint(0,1)
        if self.adjunct_status == 0:
            self.adjunct_status = "Inactive"
        elif self.adjunct_status == 1:
            self.adjunct_status = "Active"
    
    def adjunct_print(self):
        print(f"Adjunct Status: {self.adjunct_status}")

class Student_Worker(Student, Employee):
    def __init__(self, fullname, student_id, student_wage):
        super().__init__(fullname, student_id)
        self.student_wage = random.randrange(0,20000)

    def student_worker_print(self):
        print(f"Their Student ID # is: 2024-SW-{self.student_id}.\nTheir annual wage is: ${self.student_wage}")

class Alumni(Affiliate):
    def __init__(self, fullname, alumni_number):
        super().__init__(fullname)
        self.alumni_number = (random.randrange(0,10))
    
    def alumni_print(self):
        print(f"\nDatabase Details:\n{self.fullname} an allumni.\nTheir alumni # is: {self.alumni_number}")

def user_onboarding():
    fullname = ""
    status = ""
    student_id = 0
    adjunct_status = ""
    student_wage = 0
    alumni_number = 0

    fullname = input("Welcome to user onboarding!\nPlease type your fullname: ")
    user_type = input("Are you student (1) or faculty (2)? (Please type a number): ")

    def student_info():
        alumni_status = input("Are you a graduated Alumni? (1 for no, 2 for yes): ")
        if alumni_status == '1':
            student_status()
        elif alumni_status == '2':
            affiliate_call()
            alumni = Alumni(fullname, alumni_number)
            alumni.alumni_print()

    def student_status():
        student_state = input("Will you be a student worker this semester? (1 for no, 2 for yes): ")
        if student_state == '1':
            affiliate_call()
            student = Student(fullname, student_id)
            student.student_print()
        elif student_state == '2':
            affiliate_call()
            employed = Employee(status)
            employed.employee_print()
            student_worker = Student_Worker(fullname, student_id, student_wage)
            student_worker.student_worker_print()    

    def faculty_info():
        employed = print("Welcome valued faculty member!")
        department = input("For Professors, please submit your department here: ")
        adjunct_ask = input("Are you serving as an Adjunct Professor this semester? (1 for no, 2 for yes): ")
        if adjunct_ask == '1':
            affiliate_call()
            employed = Employee(status)
            employed.employee_print()
            professor = Professor(department)
            print(f"{fullname} is a professor.")
            professor.professor_print()
        elif adjunct_ask == '2':
            affiliate_call()
            employed = Employee(status)
            employed.employee_print()
            adjunct = Adjunct(department, adjunct_status)
            print(f"{fullname} is an adjunct professor.")
            adjunct.adjunct_print()

    def affiliate_call():
        affiliate = Affiliate(fullname)
        affiliate.affiliate_print()

    if user_type == '1':
        student_info()
    elif user_type == '2':
        faculty_info()

user_onboarding()