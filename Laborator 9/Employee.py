class Employee:
    def __init__(self, name, salary):
        if not name:
            raise ValueError("Numele nu poate fi gol")
        if salary <= 0:
            raise ValueError("Salariul trebuie sa fie pozitiv")

        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Angajat: {self.name}, Salariu: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)

        if not department:
            raise ValueError("Departamentul nu poate fi gol")

        self.department = department

    def get_details(self):
        return f"Manager: {self.name}, Salariu: {self.salary}, Departament: {self.department}"

try:
    print("Introduceti datele angajatului")
    emp_name = input("Nume: ")
    emp_salary = float(input("Salariu: "))

    emp = Employee(emp_name, emp_salary)

    print("\nIntroduceti datele managerului")
    mgr_name = input("Nume: ")
    mgr_salary = float(input("Salariu: "))
    mgr_department = input("Departament: ")

    mgr = Manager(mgr_name, mgr_salary, mgr_department)

    print("\nDetalii angajat:")
    print(emp.get_details())

    print("\nDetalii manager:")
    print(mgr.get_details())

except ValueError as e:
    print("Eroare:", e)

