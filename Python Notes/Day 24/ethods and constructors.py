
### 1. Constructors

'''A constructor is a special method used to initialize an object's attributes.

In Python, `__init__()` is used as a constructor. It is automatically called when an object is created.

### 2. self Keyword

`self` refers to the current object.

It is used to access instance variables and methods inside a class.

### 3. Methods

Methods are functions defined inside a class. They are used to perform actions or define the behavior of objects.

### 4. Method Overloading

Python does not support traditional method overloading like some other programming languages.

Similar behavior can be achieved using:

* Default arguments
* `*args`
* `**kwargs`

### 5. Method Overriding

Method overriding occurs when a child class provides its own implementation of a method that is already defined in the parent class.

It is commonly used to achieve runtime polymorphism.

### 6. Operator Overloading

Operator overloading allows operators such as `+`, `-`, `*`, and `==` to work with objects.

Python uses special methods, also called **dunder methods**, for operator overloading.

Examples:

* `__add__()` → `+`
* `__sub__()` → `-`
* `__mul__()` → `*`
* `__eq__()` → `==`

## What I Practiced

* Creating constructors using `__init__()`
* Using the `self` keyword
* Creating instance methods
* Using default arguments for flexible methods
* Implementing method overriding
* Understanding runtime polymorphism
* Using inheritance
* Implementing operator overloading

## Key Takeaway

Today's session helped me understand how constructors initialize objects, how `self` connects objects with their data and methods, and how overloading and overriding provide flexibility in OOP.

These concepts are important for developing reusable, maintainable, and scalable Python applications.'''


#constructor
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Nilufer", 21)

print("Name:", student.name)
print("Age:", student.age)


#self keyword
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)


student = Student("Nilufer")
student.display()


#instance method
class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()

print("Addition:", calc.add(10, 20))
print("Multiplication:", calc.multiply(5, 4))


#method overloading using default  arrguments
class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c


calc = Calculator()

print(calc.add(10))
print(calc.add(10, 20))
print(calc.add(10, 20, 30))


#method overloading *arguments
class Calculator:

    def add(self, *numbers):
        return sum(numbers)


calc = Calculator()

print(calc.add(10))
print(calc.add(10, 20))
print(calc.add(10, 20, 30, 40))


#method overriding
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


animal = Animal()
dog = Dog()

animal.sound()
dog.sound()



#runtime polymorphism
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()

#operator overloading
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


num1 = Number(10)
num2 = Number(20)

print("Result:", num1 + num2)





