class Employee:
    def __init__(self, id, name, salary):
        super().__init__()
        self.id = id
        self.name = name
        self.salary = salary

    def info(self):
        print("Id:", self.id)
        print("Name:", self.name)
        print("salary:", self.salary)

class Developer(Employee):
    def __init__(self, id, name, salary, deskId):
        super().__init__(id, name, salary)
        self.deskId = deskId

    def display(self):
        super().info()
        print("DeskId:", self.deskId)

class Manager(Employee):
    def __init__(self, id, name, salary, cabinId):
        super().__init__(id, name, salary)
        self.cabinId = cabinId

    def display(self):
        super().info()
        print("CabinId:", self.cabinId)

class Director:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print("Id:", self.id)
        print("Name:", self.name)
        print("salary:", self.salary)        

class Company:

    def __init__(self, name, employees):
        super().__init__()
        self.name = name
        self.employees = employees

    def hire(self, emp):
        self.employees.append(emp)

    def info(self):
        print("Name:", self.name)
        for emp in self.employees:
            emp.display()

dev1 = Developer(1, "ABC", 10000, 101)
man1 = Manager(2, "PQR", 20000, 201)
emps = [dev1, man1]
com = Company("XYZ", emps)
com.info()
dev2 = Developer(3, "LMN", 12000, 102)
com.hire(dev2)
man2 = Manager(4, "DEF", 30000, 202)
com.hire(man2)
dir1 = Director(5, "JKL", 50000)
com.hire(dir1)
com.info()