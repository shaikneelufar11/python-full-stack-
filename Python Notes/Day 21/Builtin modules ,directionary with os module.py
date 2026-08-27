# ============================================================
# Python Built-in Modules - Coding Examples
# ============================================================


# ============================================================
# 1. OS MODULE
# ============================================================

import os

# Current working directory
print("Current Directory:", os.getcwd())

# Change working directory
# os.chdir("path")

# List files and folders
print(os.listdir("."))

# Create a directory
if not os.path.exists("example_folder"):
    os.mkdir("example_folder")
    print("Folder created")
else:
    print("Folder already exists")

# Create a subfolder
main_folder = "example_folder"
sub_folder = os.path.join(main_folder, "SubFolder")

if not os.path.exists(sub_folder):
    os.mkdir(sub_folder)
    print("Subfolder created")
else:
    print("Subfolder already exists")

# List files/folders inside a directory
files = os.listdir(main_folder)
print("Contents:", files)

# Display each file/folder name
for item in os.listdir(main_folder):
    print(item)

# Display full paths
for item in os.listdir(main_folder):
    print(os.path.join(main_folder, item))


# ============================================================
# 2. CREATE A FILE INSIDE A FOLDER
# ============================================================

file_path = os.path.join(main_folder, "myfile.txt")

with open(file_path, "w") as f:
    f.write("Hello! This is a file inside the folder.")

print("File created:", file_path)


# ============================================================
# 3. CREATE AN EMPTY FILE
# ============================================================

empty_file = os.path.join(main_folder, "empty.txt")

open(empty_file, "w").close()

print("Empty file created")


# ============================================================
# 4. DELETE A FILE
# ============================================================

if os.path.exists(empty_file):
    os.remove(empty_file)
    print("File deleted")
else:
    print("File not found")


# ============================================================
# 5. DELETE AN EMPTY DIRECTORY
# ============================================================

# First remove the file so the folder becomes empty
if os.path.exists(file_path):
    os.remove(file_path)

if os.path.exists(sub_folder):
    os.rmdir(sub_folder)
    print("Subfolder removed")


# ============================================================
# 6. SHUTIL - DELETE NON-EMPTY DIRECTORY
# ============================================================

import shutil

# shutil.rmtree("example_folder")

# WARNING:
# rmtree() deletes the folder and everything inside it.


# ============================================================
# 7. SYS MODULE
# ============================================================

import sys

print("Python Version:", sys.version)

# Command-line arguments
print("Arguments:", sys.argv)

# Module search paths
print("Module Search Paths:", sys.path)

# Exit program
# sys.exit()


# ============================================================
# 8. PLATFORM MODULE
# ============================================================

import platform

print("Operating System:", platform.system())
print("OS Release:", platform.release())
print("Processor:", platform.processor())


# ============================================================
# 9. JSON MODULE
# ============================================================

import json

data = {
    "name": "Alice",
    "age": 30
}

# Python object -> JSON string
json_string = json.dumps(data)

print("JSON String:", json_string)

# JSON string -> Python object
parsed_data = json.loads(json_string)

print("Name:", parsed_data["name"])

# Write JSON data to a file
with open("data.json", "w") as file:
    json.dump(data, file)

# Read JSON data from a file
with open("data.json", "r") as file:
    data_from_file = json.load(file)

print("Data from file:", data_from_file)


# ============================================================
# 10. MATH MODULE
# ============================================================

import math

print("Pi:", math.pi)
print("Euler's Number:", math.e)

print("Square Root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Ceiling:", math.ceil(4.2))
print("Floor:", math.floor(4.8))
print("Absolute Value:", math.fabs(-10))
print("Factorial:", math.factorial(5))
print("GCD:", math.gcd(12, 8))
print("Log:", math.log(10, 10))

print("Sine:", math.sin(math.pi / 2))
print("Cosine:", math.cos(0))
print("Tangent:", math.tan(math.pi / 4))

print("Degrees:", math.degrees(math.pi))
print("Radians:", math.radians(180))


# ============================================================
# 11. RANDOM MODULE
# ============================================================

import random

# Random float from 0.0 to less than 1.0
print("Random:", random.random())

# Random integer
print("Random Integer:", random.randint(1, 100))

# Random float between two values
print("Random Float:", random.uniform(1, 10))

# Random element
fruits = ["apple", "banana", "cherry"]

print("Random Fruit:", random.choice(fruits))

# Multiple random selections
print("Random Choices:", random.choices(fruits, k=2))

# Shuffle a list
numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print("Shuffled List:", numbers)

# Set seed for reproducible results
random.seed(10)

print("Seeded Random Number:", random.randint(1, 100))


# ============================================================
# 12. COLLECTIONS - COUNTER
# ============================================================

from collections import Counter

data = ["a", "b", "a", "c", "a", "b"]

counter = Counter(data)

print("Counter:", counter)


# ============================================================
# 13. COLLECTIONS - DEFAULTDICT
# ============================================================

from collections import defaultdict

dd = defaultdict(int)

dd["missing"] += 1

print("Default Value:", dd["missing"])


# ============================================================
# 14. COLLECTIONS - DEQUE
# ============================================================

from collections import deque

numbers = deque([1, 2, 3])

numbers.append(4)
numbers.appendleft(0)

print("Deque:", numbers)

numbers.pop()
numbers.popleft()

print("After Removal:", numbers)


# ============================================================
# 15. ITERTOOLS - COMBINATIONS
# ============================================================

import itertools

combinations = itertools.combinations("ABCD", 2)

print("Combinations:", list(combinations))


# ============================================================
# 16. ITERTOOLS - PERMUTATIONS
# ============================================================

permutations = itertools.permutations("ABC", 2)

print("Permutations:", list(permutations))