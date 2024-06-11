class Employee:
    def __init__(self, first, last, pay ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


a1 = Employee("Jon1", "Martin1", 120)
print(a1.fullname())
a2 = Employee("Jon2", "Martin2", 120)
print(a2.fullname())
print(Employee.fullname(a1))


