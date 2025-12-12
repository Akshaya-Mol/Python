# A company wants to create a simple system to define and display employee profiles based on 
# their role types for record-keeping purposes. You are tasked with creating classes to represent 
# different types of individuals in Python. Complete the following steps:


# 1. Create a class Person with attributes name (string) and age (integer), and a method show_details() 
# that prints the person’s name and age.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_details(self):
        print(f"Hi I am {self.name} and i'm {self.age} years old")
obj1 = Person("Achu",25)
obj1.show_details()

# 2. Create a class Employee that inherits from Person, adds an attribute employee_id (string), and includes a show_details() 
# method to print the employee’s name, age, and employee ID.

class Employee(Person):
    def __init__(self, name, age,employeeID):
        Person.__init__(self,name, age)
        self.empolyee_id = employeeID
    def show_details(self):
        print(f"Hi I am {self.name} and i'm {self.age} years old and my ID is {self.empolyee_id}")

obj2 = Employee("Vishnu",30,"55AV")
obj2.show_details()

# 3. Create a class PartTime that inherits from Person, adds an attribute working_hours (float), and includes a show_details() 
# method to print the part-time worker’s name, age, and working hours.

class PartTime(Person):
    def __init__(self, name, age,workinghrs):
        Person.__init__(self,name, age)
        self.working_hours = workinghrs
    def show_details(self):
        print(f"Hi I am {self.name} and i'm {self.age} years old and my working hour is {self.working_hours}")

obj3 = PartTime("Varun",25,15.30)
obj3.show_details()

# 4. Create a class Consultant that inherits from both Employee and PartTime, adds an attribute project_name (string), and includes a show_details() 
# method to print the consultant’s name, age, employee ID, working hours, and project name.

class Consultant(Employee,PartTime):
    def __init__(self,name,age,employeeID,workinghrs,projectName):
        # super().__init__(name=name, age=age, employeeID=employeeID, workinghrs=workinghrs)
        Employee.__init__(self,name,age,employeeID)
        PartTime.__init__(self,name,age,workinghrs)
        # super().__init__(name,age,employeeID,workinghrs,projectName)
        self.project_name = projectName
    def show_details(self):
        print(f"Hi I am {self.name} and i'm {self.age} years old my Id is {self.empolyee_id} and my working hour is {self.working_hours} and my Project is {self.project_name} ")

obj4 = Consultant("Tharun",26,"55BV",22.33,"Asset Management")    
obj4.show_details()  

# 5. Create one object of each class (Person, Employee, PartTime, Consultant) with sample data.
# Display the details of each object by calling its show_details() method

p = Person("Arun", 30)
e = Employee("Meera", 28, "E102")
pt = PartTime("Ravi", 22, 20.5)
c = Consultant("Priya", 35, "C205", 15.0, "AI Development")


p.show_details()
e.show_details()
pt.show_details()
c.show_details()