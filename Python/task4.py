# A fitness center wants to create a simple system to define and display staff profiles based 
# on their roles for record-keeping purposes. You are tasked with creating a Python program to represent different types of staff. Complete the following steps:

# 1. Define a base class Employee with attributes name (string) and role (string), and a method display() 
# that prints the employee’s name and role.
class Employee:
    def __init__(self,name,role):
        self.name = name
        self.role = role
    def display(self):
        print(f"Name:",self.name,",Role:",self.role)

obj1 = Employee("kiran","developer")
obj1.display()

# 2. Create a class Trainer that inherits from Employee, adds an attribute specialization (string), and includes a display() 
# method to print the trainer’s name, role, and specialization.
class Trainer(Employee):
    def __init__(self, name, role,specialization):
        Employee.__init__(self,name, role)
        self.specialization = specialization
    def display(self):
        print(f"Name:",self.name,", Role:",self.role,", Specialization:",self.specialization)
obj2 = Trainer("Varun","Developer","React")
obj2.display()

# 3. Create a class YogaInstructor that inherits from Employee, adds an attribute yoga_style (string), and includes a display()
#  method to print the yoga instructor’s name, role, and yoga style.
class YogaInstructor(Employee):
    def __init__(self, name, role,yoga_style):
        Employee.__init__(self,name, role)
        self.yogaStyle = yoga_style
    def display(self):
        print(f"Yoga Instructor Name:",self.name,", Role:",self.role,", Style:",self.yogaStyle)
obj3 = YogaInstructor("Dinesh","Instructor","Free Style")
obj3.display()

# 4. Create a class MultiTrainer that inherits from both Trainer and YogaInstructor, includes both specialization and yoga_style attributes, and has a display()
#  method to print the multi-trainer’s name, role, specialization, and yoga style.
class MultiTrainer(Trainer,YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Trainer.__init__(self,name,role,specialization)
        YogaInstructor.__init__(self,name,role,yoga_style)
    def display(self):
        print(f"Yoga Instructor Name:",self.name,", Role:",self.role,", Specialization:",self.specialization,", Style:",self.yogaStyle)
obj4 = MultiTrainer("Vishnu","Cardio Instructor","Cardio","Free Style")        
obj4.display()

# 5.Create one object from each class (Employee, Trainer, YogaInstructor, MultiTrainer) with sample data.
# Display the details of each object by calling its display() method
emp = Employee("Arun", "Receptionist")
trainer = Trainer("Meera", "Trainer", "Weight Training")
yoga_instr = YogaInstructor("Priya", "Yoga Instructor", "Hatha Yoga")
multi_trainer = MultiTrainer("Ravi", "MultiTrainer", "CrossFit", "Ashtanga Yoga")

emp.display()
trainer.display()
yoga_instr.display()
multi_trainer.display()

