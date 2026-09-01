from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @abstractmethod
    def display(self):
        pass

    def get_age(self):
        return self.__age


class Student(Person):

    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display(self):
        print("Student Name:", self.name)
        print("Roll No:", self.roll_no)


class Faculty(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def display(self):
        print("Faculty Name:", self.name)


student = Student("Neelufar", 25, 101)
faculty = Faculty("bunny", 27)

student.display()
faculty.display()

print("Student Age:", student.get_age())
print("Faculty Age:", faculty.get_age())