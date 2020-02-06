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

    def info(self):
        super().info()
        print("DeskId:", self.deskId)

class Manager(Employee):
    def __init__(self, id, name, salary, cabinId):
        super().__init__(id, name, salary)
        self.cabinId = cabinId

    def display(self):
        # super().info()
        print("CabinId:", self.cabinId)


dev1 = Developer(1, "ABC", 10000, 101)
man1 = Manager(2, "PQR", 20000, 201)

dev1.info()
man1.display()
dev1.salary = 12000
dev1.info()