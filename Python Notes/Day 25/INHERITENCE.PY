'''Common functionality can be placed in the parent class while each child can have its own behavior.

### 5. Hybrid Inheritance

Hybrid inheritance is a combination of two or more types of inheritance.

It can create more complex class structures, and Python's MRO helps determine the correct order for method execution.

### 6. super() Method

The `super()` function is used to access methods and constructors of the parent class.

It helps reuse parent-class code without writing the same code again.

Example:

```python
class Child(Parent):

    def __init__(self):
        super().__init__()
```

## Method Resolution Order (MRO)

MRO defines the order in which Python searches for methods in an inheritance hierarchy.

We can check the MRO using:

```python
ClassName.mro()
```

or:

```python
ClassName.__mro__
```

## Advantages of Inheritance

* Code reusability
* Reduces code duplication
* Better code organization
* Easier maintenance
* Supports hierarchical relationships
* Improves scalability

## What I Practiced

* Implementing different types of inheritance
* Creating parent and child classes
* Reusing parent class properties and methods
* Using multiple inheritance
* Creating multilevel and hierarchical inheritance
* Understanding hybrid inheritance
* Using `super()` to access parent class methods
* Understanding Method Resolution Order (MRO)

## Key Takeaway

Inheritance allows Python classes to reuse and extend existing functionality. Learning different types of inheritance and the `super()` method helps in creating cleaner, reusable, and maintainable OOP programs.'''


#single inheritence
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()


#single inheritence with constructor
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def display(self):
        print("Student Name:", self.name)


student = Student("Nilufer")

student.display()


#multiple inheritence
class Father:

    def father_property(self):
        print("Father's property")


class Mother:

    def mother_property(self):
        print("Mother's property")


class Child(Father, Mother):

    def child_property(self):
        print("Child's property")


child = Child()

child.father_property()
child.mother_property()
child.child_property()


#multilevel inheritence
class Grandparent:

    def grandparent_method(self):
        print("Grandparent class")


class Parent(Grandparent):

    def parent_method(self):
        print("Parent class")


class Child(Parent):

    def child_method(self):
        print("Child class")


child = Child()

child.grandparent_method()
child.parent_method()
child.child_method()


#hirerarichal inheritence
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


class Cat(Animal):

    def meow(self):
        print("Cat is meowing")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()


#hybrid inheritence
class A:

    def show_a(self):
        print("Class A")


class B(A):

    def show_b(self):
        print("Class B")


class C(A):

    def show_c(self):
        print("Class C")


class D(B, C):

    def show_d(self):
        print("Class D")


obj = D()

obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()
