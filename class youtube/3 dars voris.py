class Employee2:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


class Develop(Employee2):
    def __init__(self, first, last, pay, lang_1):
        super().__init__(first, last, pay)
        self.lang_1 = lang_1


class Manager(Employee2):
    def __init__(self, first, last, pay, lang_2=None):
        super().__init__(first, last, pay)
        if lang_2 is None:
            self.lang_2 = []
        else:
            self.lang_2 = lang_2

    def add_1(self, emp):
        if emp not in self.lang_2:
            self.lang_2.append(emp)

    def remove_1(self, emp):
        if emp in self.lang_2:
            self.lang_2.remove(emp)

    def print_1(self, emp):
        if emp in self.lang_2:
            print("-->", emp.fullname())


a1 = Employee2("Jon1", "Martin1", 120)
a2 = Employee2("Jon2", "Martin2", 120)
d1 = Develop("Jon2", "Martin2", 120, "python")
d2 = Develop("Jon1", "Martin1", 120, "C#")
m1 = Manager("Jon1", "Martin1", 120, [d1])
m1.add_1(d2)
m1.print_1(d2)
m1.remove_1(d2)
m1.print_1(d1)
print(isinstance(a1, Employee2))

