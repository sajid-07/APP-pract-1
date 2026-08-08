def star(func):
    def wrapper():
        return "*** " + func() + " ***"
    return wrapper

class Student:
    college = "MIT"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_college(cls, cname):
        cls.college = cname

    @star
    def show(self):
        return self.name

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

s1 = Student("Avani")

print(s1)
print(len(s1))
print(s1.show())

Student.change_college("MIT ADT")
print(Student.college)