class Employee:
    def __init__(self, first, last, pay ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return 'Employed ({}, {}, {})'.format(self.first, self.last, self.pay)

    def __str__(self):
        return '{}, {}'.format(self.first, self.last)

    def __add__(self, other):
        return self.pay+other.pay

    def __len__(self):
        return len(self.fullname())


a1 = Employee("Jon1", "Martin1", 120)
a2 = Employee("Jon2", "Martin2", 130)
print(a1)
print(a1.__repr__())
print(a1.__str__())
print(int.__add__(1, 2))
print(a1+a2)
print()


