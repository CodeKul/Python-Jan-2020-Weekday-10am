class Employee:

    def __init__(self, name, id, salary, desig, age, raise_sal):
        super().__init__()
        self.name = name
        self.id = id
        self.salary = salary
        self.desig = desig
        self.age = age
        self.raise_sal = raise_sal

    def info(self):
        print('Name:',self.name)
        print('id:', self.id)
        print('salary:', self.salary)
        print('Designation:', self.desig)
        print('Age:', self.age)

    def increment(self):
        self.salary += self.salary * self.raise_sal

    def promote(self, desig, shouldInrcr):
        self.desig = desig
        if(shouldInrcr):
            self.increment()
    

emp1 = Employee('ABC', 1, 10000, 'Developer', 25, 0.30)
emp1.info()
emp1.promote("Sr. Developer", False)
emp1.info()

emp2 = Employee('PQR', 2, 12000, 'Manager', 30, 0.40)

class Company:

    def __init__(self, name, employees):
        super().__init__()
        self.name = name
        self.employees = employees
    
    def display(self):
        print("Name:", self.name)
        print("Count:", len(self.employees))

    def display_employees(self):
        for emp in self.employees:
            emp.info()
    
    def annual_promotion(self):
        for emp in self.employees:
            emp.increment()
    

com = Company("XYZ", [emp1, emp2])
com.display()
com.display_employees()
com.annual_promotion()
com.display_employees()