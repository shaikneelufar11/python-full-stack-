

## Topics Covered

'''* Introduction to OOP
* Advantages of OOP
* Classes and Objects
* Creating single and multiple objects
* Attributes and accessing attributes
* Instance Attributes
* Class Attributes
* Methods and calling methods
* `self` keyword
* `__init__()` Constructor'''

## Practice Code

#python
class Student:

    college = "ABC College"

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)
        print("College:", self.college)


student1 = Student("Nilufer", "Bioinformatics")
student2 = Student("Rahul", "Computer Science")

student1.display()
print()
student2.display()


## Key Concepts

'''**Class:** A blueprint used to create objects.

**Object:** An instance of a class.

**Attributes:** Variables that store data about an object.

**Instance Attribute:** Data specific to an individual object.

**Class Attribute:** A common attribute shared by objects.

**Method:** A function defined inside a class that represents an object's behavior.

**self:** Refers to the current object.

**`__init__()` :** Constructor used to initialize object attributes.'''

## What I Practiced

'''* Creating classes and objects
* Creating multiple objects
* Defining and accessing attributes
* Using instance and class attributes
* Creating and calling methods
* Using constructors
* Building a simple calculator using a class'''

## Key Takeaway

#OOP helps make Python programs more organized, reusable, and easier to maintain. Today I understood how classes, objects, attributes, and methods work together to build structured programs.
#simple objects
class Student:
    name = "Nilufer"
    course = "Bioinformatics"

student1 = Student()

print(student1.name)
print(student1.course)

#multiple objects
class Student:
    pass

student1 = Student()
student2 = Student()

student1.name = "Nilufer"
student2.name = "Rahul"

print("Student 1:", student1.name)
print("Student 2:", student2.name)

#instance attribute

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Nilufer", 21)
student2 = Student("Anu", 22)

print(student1.name, student1.age)
print(student2.name, student2.age)


#class attribute
class Student:

    college = "ABC College"

    def __init__(self, name):
        self.name = name


student1 = Student("Nilufer")
student2 = Student("Rahul")

print(student1.name, student1.college)
print(student2.name, student2.college)

#methods
class Student:

    def __init__(self, name):
        self.name = name

    def study(self):
        print(self.name, "is studying")

    def attend_class(self):
        print(self.name, "is attending class")


student1 = Student("Nilufer")

student1.study()
student1.attend_class()


#employee class
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


employee1 = Employee("Nilufer", 30000)

employee1.display()




