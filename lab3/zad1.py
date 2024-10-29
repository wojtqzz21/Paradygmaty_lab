class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def wypisz(self):
        return f"Name: {self.name} Age: {self.age} Salary: {self.salary}"

class EmployeeManager:
    def __init__(self):
        self.employees = []
    def dodaj(self, name, age, salary):
        self.employees.append(Employee(name,age,salary))

    def wypisz(self):
        for employee in self.employees:
            print(employee.wypisz())
    def usun(self, min, max):
        for employee in self.employees:
            if employee.age >= min and employee.age <= max:
                self.employees.remove(employee)
    def szukaj(self, name):
        for employee in self.employees:
            if name == employee.name:
                print("Jest: ", employee.wypisz())
            else:
                print("Niema")

    def akt(self, name, salary):
        for employee in self.employees:
            if name == employee.name:
                employee.salary = salary

class FrontendManager:
    def __init__(self, x):
        self.x = EmployeeManager()

    def dodaj(self):
        a = input("Podaj name: ")
        b = input("Podaj wiek: ")
        c = input("Podaj salare: ")
        self.x.dodaj(a, b, c)
    def wypisz(self):
        self.x.wypisz()




# d = EmployeeManager()
# d.dodaj("a", 1, 2)
# d.dodaj("b", 2, 3)
# d.wypisz()
# d.akt("a", 1234)
# d.wypisz()
# d.dodaj()
# d.wypisz()
# d.usun(10,20)
# d.wypisz()
# d.szukaj("John")

f = FrontendManager(1)
f.dodaj()
f.wypisz()
