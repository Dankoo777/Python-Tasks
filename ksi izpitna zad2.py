class Employee:
    def __init__(self,i_num,fname,lname,work_experience,education_level,salary,age):
        self.i_num = i_num
        self.lname = lname
        self.fname = fname
        self.work_experience = work_experience
        self.education_level = education_level
        self.salary = salary
        self.age = age
    def display_info(self):
        print(f"Employee {self.i_num} info:\nNames: {self.fname} {self.lname}\nAge: {self.age}\nWork experience: {self.work_experience}\nEducation level: {self.education_level}\nSalary: {self.salary}\n\n\n")
    def bonus(self):
        salary = self.salary
        experience = self.work_experience
        if self.education_level == "Secondary":
            salary += salary / 50
        elif self.education_level == "Higher":
            salary += salary / 20
        salary += salary * (experience * (1.2 / 100))
        print(f"Salary with bonus: {salary}")


employee_list = []
n = int(input("Number of employees: "))
for i in range(n):
    i_num = input("Employee number: ")
    fname = input("First name: ")
    lname = input("Last name: ")
    work_experience = int(input("Work experience: "))
    education_level = input("Education level: ")
    salary = int(input("Salary: "))
    age = int(input("Age: "))
    employee = Employee(i_num,fname,lname,work_experience,education_level,salary,age)
    employee_list.append(employee)

for employee in employee_list:
    employee.bonus()
    

def sort_employee(lst):
    lst.sort(key = lambda x: x.age)
    for employee in lst:
        print(employee.display_info())
sort_employee(employee_list)


def search_by_name(lst):
    fname = input("Input first name to search: ")
    lname = input("Input last name to search: ")
    count = 0
    for employee in lst:
        if employee.fname == fname and employee.lname == lname:
            print(employee.display_info())
            count += 1
    if count == 0:
        print("Not Found!!!")
search_by_name(employee_list)


def print_by_education_experience(lst):
    education = input("Input searched education: ")
    experience = input("Input searched experience: ")
    for employee in lst:
        if employee.education_level == education and employee.work_experience == experience:
            print(employee.display_info())
print_by_education_experience(employee_list)


def remove_employee(lst):
    i_num = input("Input employee number to delete: ")
    count = 0
    for employee in lst:
        if employee.i_num == i_num:
            lst.remove(employee)
            print("Information deleted!!!")
            count += 1
    if count == 0:
        print("Wrong i_num!!!")
remove_employee(employee_list)