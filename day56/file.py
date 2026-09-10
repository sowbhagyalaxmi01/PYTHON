 #File handling in Python means creating, opening, reading, writing, and managing files such as .txt, .csv, .json, etc.
 # Python Program
 #       ↓
#     Data
#        ↓
#      File
 #       ↓
#  Stored permanently

 #2. Main file operations
 # Open a file
 # Read a file
 # Write to a file
 # Append to a file
 # Close a file
 # with open() — recommended way
 # File modes: r, w, a, x
 # Reading line by line
 # Working with CSV files
# Working with JSON files


# # Why do we use files?
 # To store data permanently.
 # To retrieve data later.
 # To handle large amounts of data.
 # To share data between programs.



# File Modes
#  Mode	Meaning
# r	Read
#  w	Write; overwrites existing content
#  a	Append data at the end
#  x	Create a new file
#  r+	Read and write



# Why Do We Need Files?
# Imagine you create a student management program.
# Without files:
# Program starts
#    ↓
# Student data entered
#    ↓
# Program closes
#    ↓
# Data LOST ❌


# With files:
# Program starts
#    ↓
# Student data entered
#    ↓
# Save to file
#    ↓
# Program closes
#    ↓
# Data remains ✅
# So the main purpose of files is:
# To store and retrieve data permanently.



# A file is a place where data is stored permanently.

# For example:

# student.txt
# employees.csv
# config.json
# image.jpg
# data.pdf