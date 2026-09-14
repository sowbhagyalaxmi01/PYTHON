# Python File Handling — Notes
# 1. File Paths
# A path tells Python where a file or folder is located.
# Two main types:
# Absolute path → complete location.
# Relative path → location relative to the current working directory.
# Example absolute path:
# C:\Users\User\Desktop\data.txt
# Example relative path:
# data\data.txt
# . → current directory.
# .. → parent directory.
# Paths are important when working with files and folders.
# pathlib is preferred for modern path handling.



# 2. os Module
# os allows Python to interact with the operating system.
# Import:
# import os
# os.getcwd() → gets current working directory.
# os.chdir() → changes current working directory.
# os.listdir() → lists files/folders.
# os.mkdir() → creates a directory.
# os.makedirs() → creates nested directories.
# os.rename() → renames a file/folder.
# os.remove() → deletes a file.
# os.rmdir() → deletes an empty directory.
# os.path.exists() → checks whether path exists.
# os.path.isfile() → checks whether it is a file.
# os.path.isdir() → checks whether it is a directory.
# os.path.join() → safely joins path parts.



# 3. pathlib
# pathlib provides an object-oriented way to work with paths.
# Import:
# from pathlib import Path
# Path() → creates a path object.
# .exists() → checks existence.
# .is_file() → checks if it is a file.
# .is_dir() → checks if it is a directory.
# .mkdir() → creates directory.
# .iterdir() → loops through directory contents.
# .unlink() → deletes a file.
# .rename() → renames a file/folder.
# .parent → gets parent directory.
# .name → gets file/folder name.
# .suffix → gets file extension.
# / can be used to join paths.
# Example:
# path = Path("data") / "student.csv"
# Remember:
# os       → traditional/common
# pathlib  → modern/professional ⭐



# 4. CSV Files ⭐⭐⭐
# CSV = Comma-Separated Values.
# Used for tabular data.
# Data is organized into rows and columns.
# Common in:
# Data Science
# Machine Learning
# Excel data
# Reports
# Datasets
# Python provides the csv module.
# Import:
# import csv
# csv.reader() → reads CSV rows.
# csv.writer() → writes CSV rows.
# writerow() → writes one row.
# writerows() → writes multiple rows.
# DictReader → reads rows as dictionaries.
# DictWriter → writes dictionaries to CSV.
# CSV usually has a header.
# Example structure:
# name,age,course
# Laxmi,21,B.Tech
# Ravi,22,B.Tech
# Data Science connection:
# CSV
#  ↓
# Pandas
#  ↓
# Data Cleaning
#  ↓
# Data Analysis
#  ↓
# ML



# 5. JSON Files ⭐⭐⭐
# JSON = JavaScript Object Notation.
# Used for storing and exchanging structured data.
# Very common in:
# APIs
# Web applications
# AI/ML projects
# Configuration files
# Data exchange
# Python provides the json module.
# Import:
# import json
# Important functions:
# json.load() → JSON file → Python object.
# json.loads() → JSON string → Python object.
# json.dump() → Python object → JSON file.
# json.dumps() → Python object → JSON string.
# Common conversions:
# JSON object → Python dictionary
# JSON array  → Python list
# Remember:
# load   → file → Python
# loads  → string → Python
# dump   → Python → file
# dumps  → Python → string


# ⭐ Quick Revision Table
# Topic	Main Purpose	Important Things
# File Paths	Locate files/folders	Absolute, Relative
# os	OS/file operations	listdir, mkdir, remove
# pathlib	Modern path handling	Path, exists, iterdir
# CSV	Tabular data	reader, writer, DictReader
# JSON	Structured data	load, loads, dump, dumps


