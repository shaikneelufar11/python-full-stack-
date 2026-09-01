# Exception Handling in Python

try:
    # Taking user input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Division operation
    result = num1 / num2
    print("Division Result:", result)

    # List Index Exception
    numbers = [10, 20, 30]
    index = int(input("Enter list index: "))
    print("List Value:", numbers[index])

    # Custom Exception
    age = int(input("Enter your age: "))

    if age < 18:
        raise Exception("Not eligible for voting")
    else:
        print("Eligible for voting")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Please enter only numbers")

except IndexError:
    print("Error: List index out of range")

except Exception as e:
    print("Custom Exception:", e)

else:
    print("All operations completed successfully")

finally:
    print("Program execution completed")