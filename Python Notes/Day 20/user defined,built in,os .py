# Python Modules and File & Directory Handling

## 1. Modules

'''A **module** is a Python `.py` file containing functions, classes, variables, and executable code. Modules help organize, reuse, maintain, and debug code.

### Advantages

* Code Reusability
* Better Code Organization
* Reduces Code Duplication
* Easier Debugging
* Easier Maintenance
* Team Collaboration

### Types of Modules

1. **User-Defined Modules** — Created by programmers.
2. **Built-in Modules** — Provided by Python, such as `math`, `os`, `random`, `sys`.
3. **Third-Party Modules** — Installed using `pip`.'''



## 2. Importing Modules


# Import entire module
import my_module
print(my_module.greet("Rahul"))

# Import specific function
from my_module import greet
print(greet("Rahul"))

# Import multiple functions
from math import sqrt, factorial
print(sqrt(25))
print(factorial(5))

# Import using alias
import my_module as mm
print(mm.greet("Rahul"))

'''# Import everything - not recommended
from math import *
print(sqrt(16))
```

`from module import *` is generally not recommended because it can create name conflicts.'''


## 3. User-Defined Modules

### my_module.py


def greet(name):
    return f"Hello, {name}!"

pi = 3.14159


'''### main.py
import my_module
print(my_module.greet("Alice"))
print(my_module.pi)


### Specific Function
from my_module import greet
print(greet("Bob"))


### Alias


import my_module as m

print(m.greet("Charlie"))'''


## 4. Module Search Path

'''Python searches for modules in:

1. Current working directory
2. Built-in modules
3. Directories listed in `sys.path`'''


import sys

print(sys.path)

sys.path.append("C:/PythonModules")

## 5. `__name__` and `__main__`

'''Every Python file has a special variable called `__name__`.

When a file is executed directly:

```python
__name__ == "__main__"
```

When the file is imported:
__name__ == "module_name"'''


### Example

def greet(name):
    return f"Hello {name}"

if __name__ == "__main__":
    print(greet("Alice"))


#This prevents the code inside the `if` block from executing when the file is imported.

### Why use it?

'''* Prevent test code from running during import
* Use the same file as a standalone program and module
* Improve code organization
* Make modules reusable'''

---

## 6. Installing Third-Party Modules


# Built-in Modules

## 7. `os` Module

#The `os` module is used to interact with the operating system.


import os

print(os.getcwd())

if not os.path.exists("example_folder"):
    os.mkdir("example_folder")


#Common functions:

'''os.getcwd()        → Current working directory
os.chdir(path)     → Change directory
os.listdir(path)   → List files and folders
os.mkdir(name)     → Create directory
os.remove(file)    → Delete file
os.rmdir(dir)      → Delete empty directory
os.path.exists()   → Check whether path exists'''


## 8. `sys` Module
import sys

print("Python Version:", sys.version)
print(sys.path)


'''Common functions:


sys.argv     → Command-line arguments
sys.exit()   → Exit program
sys.path     → Module search paths
sys.version  → Python version'''


## 9. `platform` Module


import platform

print(platform.system())
print(platform.release())
print(platform.processor())


## 10. `json` Module

#Used for JSON encoding and decoding.


import json

data = {
    "name": "Alice",
    "age": 30
}

json_str = json.dumps(data)
print(json_str)

parsed = json.loads(json_str)
print(parsed["name"])

'''json.dumps() → Python object → JSON string
json.loads() → JSON string → Python object
json.dump()  → Write JSON to file
json.load()  → Read JSON from file'''


## 11. `math` Module
import math

print(math.sqrt(25))
print(math.factorial(5))
print(math.sin(math.pi / 2))


'''Important functions:
math.sqrt()
math.pow()
math.ceil()
math.floor()
math.fabs()
math.factorial()
math.gcd()
math.log()
math.sin()
math.cos()
math.tan()
math.degrees()
math.radians()'''


'''Constants:
math.pi
math.e'''


## 12. `random` Module
import random

print(random.randint(1, 100))
print(random.choice(["apple", "banana", "cherry"]))


#Common functions:

'''random.random()
random.randint()
random.uniform()
random.choice()
random.choices()
random.shuffle()
random.seed()'''


## 13. `collections` Module
from collections import Counter, defaultdict

data = ["a", "b", "a", "c"]

counter = Counter(data)
print(counter)

dd = defaultdict(int)
dd["missing"] += 1

print(dd["missing"])


#Important classes:

'''text
Counter     → Counts frequency
defaultdict → Dictionary with default values
deque       → Double-ended queue'''


## 14. `itertools` Module
import itertools

print(list(itertools.combinations("ABCD", 2)))


#Useful functions include:

'''text
combinations()
permutations()'''

# Directory and File Handling

## 15. Create a Directory
import os

path = r"C:\Users\Jani Basha Shaik\Downloads\pythonfolder1"

if not os.path.exists(path):
    os.mkdir(path)
    print("Folder created successfully")
else:
    print("Folder already exists")


## 16. Delete an Empty Directory
import os

path = r"C:\Users\Jani Basha Shaik\Downloads\pythonfolder1"

if os.path.exists(path):
    os.rmdir(path)
    print("Folder removed successfully!")
else:
    print("Folder does not exist!")


#os.rmdir()` works only when the folder is empty.
## 17. Create a Subfolder
import os

main_folder = r"C:\Users\Jani Basha Shaik\Downloads\pythonfolder"

subfolder = os.path.join(main_folder, "bashafolder")

if not os.path.exists(subfolder):
    os.mkdir(subfolder)
    print("Subfolder created successfully")
else:
    print("Already exists")


## 18. Create an Empty File
import os

file_path = os.path.join(
    r"C:\Users\Jani Basha Shaik\Downloads\pythonfolder",
    "basha1.txt"
)

with open(file_path, "w"):
    print("File created")


#"w"` mode creates the file if it does not exist.

## 19. Create a File and Write Data
import os

file_path = os.path.join(
    r"C:\Users\Jani Basha Shaik\Downloads\pythonfolder",
    "jani.txt"
)

with open(file_path, "w") as f:
    f.write("Hello World Jani Basha")

print("File created successfully")


## 20. List Files and Folders

import os

path = r"C:\Users\Jani Basha Shaik\Downloads\pythonfolder"

items = os.listdir(path)

print(items)


## 21. Display File and Folder Names

#python
import os

path = r"C:\Users\Jani Basha Shaik\Downloads\pythonfolder"

for item in os.listdir(path):
    print(item)


## 22. Display Full Path

#python
import os

path = r"C:\Users\Jani Basha Shaik\Downloads\pythonfolder"

for item in os.listdir(path):
    print(os.path.join(path, item))

## 23. Delete a File

#python
import os

file_path = r"C:\Users\Jani Basha Shaik\Downloads\MyFolder\myfile.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully")
else:
    print("File not found")


## 24. Delete an Empty Folder

#python
import os

folder_path = r"C:\Users\Jani Basha Shaik\Downloads\MyFolder\SubFolder"

if os.path.exists(folder_path):
    os.rmdir(folder_path)
    print("Folder deleted")


## 25. Delete Folder With Files and Subfolders

#python
import shutil

path = r"C:\Users\Jani Basha Shaik\Downloads\pythonfolder"

if os.path.exists(path):
    shutil.rmtree(path)
    print("Folder deleted successfully")


'''---

# Quick Reference

| Operation                   | Method                     |
| --------------------------- | -------------------------- |
| Create directory            | `os.mkdir()`               |
| Delete empty directory      | `os.rmdir()`               |
| List directory              | `os.listdir()`             |
| Check path                  | `os.path.exists()`         |
| Join paths                  | `os.path.join()`           |
| Delete file                 | `os.remove()`              |
| Delete folder with contents | `shutil.rmtree()`          |
| Create/write file           | `open(path, "w")`          |
| Append to file              | `open(path, "a")`          |
| Module search paths         | `sys.path`                 |
| Install package             | `pip install package_name` |'''

## Key Takeaways

'''* Modules help organize and reuse Python code.
* User-defined modules are created by programmers.
* Built-in modules provide ready-to-use functionality.
* `__name__ == "__main__"` controls code execution when a file is run directly.
* `os` is useful for file and directory operations.
* `os.path.join()` creates paths correctly.
* `shutil.rmtree()` removes folders containing files and subfolders.
* `json`, `math`, `random`, `collections`, and `itertools` provide useful built-in functionality.'''




