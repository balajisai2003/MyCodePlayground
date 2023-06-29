class Employee:
    no_of_employee = 0
    inc = 1.5

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employee += 1

    def increment(self):
        self.salary *= self.inc

    @classmethod
    def ChangeInc(cls, amount):
        cls.inc = amount

    #  alternative constructor
    @classmethod
    def FromStr(cls, s):
        fname, lname, salary = s.split("-")
        return cls(fname, lname, salary)

    @staticmethod  # independent method
    def isopen(day: str):
        if day.lower() == "sunday":
            return True
        else:
            return False

    # dunder method
    def __repr__(self):
        return "Employee({}, {}, {})".format(self.fname,self.lname,self.salary)

    def __str__(self):
        return "employee name is {}".format(self.fname)
# INHERITANCE


class Progremmer(Employee):
    def __init__(self, fname, lname, salary, language, exp):
        super().__init__(fname, lname, salary)
        self.language = language
        self.exp = exp

    # overriding
    def increment(self):
        self.salary *= self.inc
balaji = Employee("balaji","nadakuditi",80909090)
print(str(balaji))
print(repr(balaji))
