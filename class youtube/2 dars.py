import time

class Employee1:
    num = 0
    raise_1 = 1.04

    def __init__(self, first, last, pay ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee1.num += 1

    def fullname(self):
        return '{} {} {}'.format(self.first, self.last, self.pay)

    def apply_raise(self, pay):
        self.pay = int(self.pay * self.raise_1)

    @classmethod
    def set_raise_(cls, amount):
        cls.raise_1 = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @classmethod
    def stap_time(cls, t):
        y, f = str(time.time()).split(".")
        return cls(y, f, t)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


a1 = Employee1("Jon1", "Martin1", 120)
a2 = Employee1("Jon2", "Martin2", 120)
a3 = Employee1.stap_time(0)
print(a3.fullname())


import datetime
my_date = datetime.date(2024, 5, 25)

print(Employee1.is_workday(my_date))



"""print(Employee1.num)
print(Employee1.raise_1)
print(Employee1.raise_1)
new_a1 = Employee1.from_string("Jon3-Martin3-1021")
print(new_a1.fullname())"""




