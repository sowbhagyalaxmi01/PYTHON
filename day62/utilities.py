#math
# Mathematical operations.
import math
math.sqrt(16)
math.pow(2, 3)
math.ceil(4.2)
math.floor(4.8)
math.factorial(5)
math.gcd(12, 18)

# math.sqrt(x) → square root
# math.pow(x, y) → x raised to y
# math.ceil(x) → round up
# math.floor(x) → round down
# math.factorial(x) → factorial
# math.gcd(a, b) → greatest common divisor




#datetime
# Dates and times.
from datetime import datetime, date, timedelta

now = datetime.now()
today = date.today()

print(now)
print(today)
print(today + timedelta(days=7))



#random
# Random numbers and selections.
import random

random.randint(1, 10)
random.random()
random.choice(["red", "blue", "green"])
random.shuffle([1, 2, 3, 4])




#os
# Operating-system operations.(Useful for files, folders, environment variables, and paths.)
import os
print(os.getcwd())
print(os.listdir())
os.mkdir("test")



# sys
# Python interpreter/system utilities.
import sys
print(sys.version)
print(sys.argv)
print(sys.path)


#pathlib
# Modern way to work with file paths.

from pathlib import Path

path = Path("data.txt")

print(path.exists())
print(path.name)
print(path.suffix)

# 7. shutil
# Copying, moving, and deleting files/folders.

import shutil

shutil.copy("a.txt", "b.txt")
shutil.move("b.txt", "folder/")

# 8. json
# Work with JSON data.

import json

data = {"name": "John", "age": 25}

text = json.dumps(data)
print(text)

data2 = json.loads(text)

# 9. re
# Regular expressions / pattern matching.

import re

text = "My phone is 9876543210"

result = re.search(r"\d+", text)

print(result.group())

# 10. collections
# Specialized data structures.

from collections import Counter

numbers = [1, 2, 2, 3, 3, 3]

print(Counter(numbers))


# Important utilities:
# Counter
# defaultdict
# deque
# namedtuple

# 11. itertools
# Powerful tools for iterating over data.

from itertools import combinations

data = [1, 2, 3]

print(list(combinations(data, 2)))

# 12. functools
# Functions that help manipulate other functions.

from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers)

print(result)

# 13. operator
# Functions corresponding to Python operators.

import operator

print(operator.add(5, 3))
print(operator.mul(5, 3))

# 14. statistics
# Basic statistical calculations.

import statistics

numbers = [10, 20, 30, 40, 50]

print(statistics.mean(numbers))
print(statistics.median(numbers))
print(statistics.mode([1, 1, 2, 3]))

# 15. decimal
# Accurate decimal arithmetic.

from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print(a + b)

# Useful when precision matters, especially financial calculations.

# 16. fractions
# Work with fractions.

from fractions import Fraction

a = Fraction(1, 2)
b = Fraction(1, 3)

print(a + b)

# 17. time
# Time-related utilities.

import time

print(time.time())

time.sleep(2)

print("Done")

# 18. calendar
# Work with calendars.

import calendar

print(calendar.month(2026, 9))
print(calendar.isleap(2028))

# 19. textwrap
# Format and wrap text.

import textwrap

text = "Python is a very useful programming language."

print(textwrap.wrap(text, width=15))

# 20. string
# Useful string constants and utilities.

import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# 21. pprint
# Pretty-print complicated data.

from pprint import pprint

data = {
    "users": [
        {"name": "John", "age": 25},
        {"name": "Alice", "age": 30}
    ]
}

pprint(data)

# 22. copy
# Copy Python objects.

import copy

a = [[1, 2], [3, 4]]

b = copy.copy(a)
c = copy.deepcopy(a)

# 23. typing
# Type hints.

from typing import List

def total(numbers: List[int]) -> int:
    return sum(numbers)

# Modern Python also supports:

def total(numbers: list[int]) -> int:
    return sum(numbers)

# 24. enum
# Create enumerations.

from enum import Enum

class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3

print(Color.RED)

# 25. dataclasses
# Create data-focused classes easily.

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int

student = Student("John", 20)

print(student)

# 26. argparse
# Build command-line programs.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name")

args = parser.parse_args()

print(args.name)

# 27. logging
# Professional application logging.

import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program started")
logging.warning("Something may be wrong")
logging.error("An error occurred")

# 28. subprocess
# Run external programs/commands.

import subprocess

result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)

print(result.stdout)

# 29. sqlite3
# Use a local SQLite database.

import sqlite3

connection = sqlite3.connect("users.db")

cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)"
)

connection.commit()
connection.close()

# 30. csv
# Read and write CSV files.

import csv

with open("users.csv", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
