
### 1. Encapsulation

'''Encapsulation is the process of wrapping data and methods together inside a class.

It helps control how the data of an object is accessed and modified.

### 2. Access Modifiers

Access modifiers define how class members can be accessed.

Python mainly uses naming conventions for:

* Public members
* Protected members
* Private members

### 3. Public Members

Public members can be accessed directly from outside the class.

Example:

```python
class Student:
    name = "Nilufer"
```

### 4. Protected Members

Protected members are represented using a single underscore `_`.

They are intended to be used within the class and its child classes.

Example:

```python
class Student:
    _course = "Bioinformatics"
```

### 5. Private Members

Private members are represented using double underscores `__`.

They are intended to restrict direct access from outside the class.

Example:

```python
class BankAccount:
    __balance = 5000
```

### 6. Getter Method

A getter method is used to safely access the value of a private variable.

Example:

```python
def get_balance(self):
    return self.__balance
```

### 7. Setter Method

A setter method is used to modify a private variable after performing validation.

Example:

```python
def set_balance(self, amount):
    if amount >= 0:
        self.__balance = amount
```

## Advantages of Encapsulation

* Protects data from unwanted modification
* Provides controlled access to data
* Allows validation before updating values
* Improves code security
* Makes programs easier to maintain
* Keeps data and related methods together

## What I Practiced

* Creating private variables
* Using public, protected, and private members
* Creating getter methods
* Creating setter methods
* Validating data before modification
* Implementing a Bank Account example
* Controlling access to sensitive account information

## Key Takeaway

Encapsulation helps protect object data by controlling how it is accessed and modified. Using private variables along with getter and setter methods makes Python programs more secure, organized, and maintainable.'''


#public acess modifier
class Student:

    def __init__(self, name):
        self.name = name


student = Student("Nilufer")

print(student.name)


#protected acess modifier
class Student:

    def __init__(self, name):
        self._name = name


student = Student("Nilufer")

print(student._name)


#private variable

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance


account = BankAccount(5000)

print(account._BankAccount__balance)

#getter method
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

print("Balance:", account.get_balance())

#setter method
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")


student = Student(80)

print("Marks:", student.get_marks())

student.set_marks(90)

print("Updated Marks:", student.get_marks())


#bank accoiunt enscapulation
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Amount withdrawn successfully")

    def get_balance(self):
        return self.__balance


account = BankAccount("Nilufer", 5000)

account.deposit(2000)
account.withdraw(1000)

print("Account Holder:", account.name)
print("Balance:", account.get_balance())


#acc num validation
class BankAccount:

    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self, entered_number):
        if entered_number == self.__account_number:
            return self.__account_number
        else:
            return "Invalid account number"

    def get_balance(self):
        return self.__balance


account = BankAccount("ACC12345", 10000)

print(account.get_account_number("ACC12345"))
print("Balance:", account.get_balance())


#complete getter and setter example
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be greater than 0")


employee = Employee("Nilufer", 30000)

print("Name:", employee.name)
print("Salary:", employee.get_salary())

employee.set_salary(35000)

print("Updated Salary:", employee.get_salary())

