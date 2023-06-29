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
    def ChangeInc(cls,amount):
        cls.inc=amount
    #  alternative constructor
    @classmethod
    def FromStr(cls,s):
        fname,lname,salary=s.split("-")
        return cls(fname,lname,salary)
    @staticmethod # independent method
    def isopen(day:str):
        if day.lower()=="sunday":
            return True
        else:
            return False




# "INHERITANCE"

class Progremmer(Employee):
    def __init__(self, fname, lname, salary, language, exp):
        super().__init__(fname, lname, salary,)
        self.language = language
        self.exp = exp
    # overriding
    def increment(self):
        self.salary *= self.inc



Balaji = Employee("balaji", "nadakuditi", 900000)
Balaji.increment()
Sai = Employee.FromStr("sai-nadakuditi-500000")
print(Employee.isopen("suNday"))
print(Sai.fname)




jay = Progremmer("jay","vardhan",45000,"python","6 yrs")
print(jay.salary)
jay.increment()
print(jay.salary)
jay.ChangeInc(3)
Sai.ChangeInc(5) # !!!!!!!!!!!
print(jay.inc,Balaji.inc,Sai.inc)