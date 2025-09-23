class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_details(self):
        print(f"Hi I am {self.name} and i'm {self.age} years old")
obj1 = Person("Achu",25)
obj1.show_details()

class Employee(Person):
    def __init__(self, name, age,employeeID):
        super().__init__(name, age)
        self.empolyee_id = employeeID
    def show_details(self):
        print(f"Hi I am {self.name} and i'm {self.age} years old and my ID is {self.empolyee_id}")

obj2 = Employee("Vishnu",30,"55AV")
obj2.show_details()

class PartTime(Person):
    def __init__(self, name, age,workinghrs):
        super().__init__(name, age)
        self.working_hours = workinghrs
    def show_details(self):
        print(f"Hi I am {self.name} and i'm {self.age} years old and my working hour is {self.working_hours}")

obj3 = PartTime("Varun",25,15.30)
obj3.show_details()

# class Consultant(Employee,PartTime):
#     def __init__(self,name,age,employeeID,workinghrs,projectName):
#         super().__init__(name=name, age=age, employeeID=employeeID, workinghrs=workinghrs)
#         # Employee.__init__(self,name,age,employeeID)
#         # PartTime.__init__(self,name,age,workinghrs)
#         # super().__init__(name,age,employeeID,workinghrs,projectName)
#         self.project_name = projectName
#     def show_details(self):
#         print(f"Hi I am {self.name} and i'm {self.age} years old my Id is {self.empolyee_id} and my working hour is {self.working_hours} and my Project is {self.project_name} ")

# obj4 = Consultant("Tharun",26,"55BV",22.33,"Asset Management")    
# obj4.show_details()