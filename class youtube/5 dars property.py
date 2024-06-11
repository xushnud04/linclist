class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{} {} @gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Deleting {} {}".format(self.first, self.last))
        self.first = None
        self.last = None


a1 = Employee("Jon1", "Martin1", 120)
a2 = Employee("Jon2", "Martin2", 120)
print(a2.fullname)
a1.fullname ="Jon3 Martin3"
print(a2.fullname)
del a1.fullname
print(a1.fullname)



