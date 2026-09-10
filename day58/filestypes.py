# Types of Files

# There are two major categories.
# A. Text files
# Human-readable data.
# Examples:
# .txt
# .csv
# .json
# .py
# .html

# Example:
# Name: Laxmi
# Age: 21
# Course: B.Tech

# B. Binary files
# Data stored as binary bytes.
# Examples:
# .jpg
# .png
# .mp3
# .mp4
# .pdf
# .exe
# You normally don't read these files directly as normal text.


#  File Path
# A path tells Python where a file is located.

# Example:
# C:\Users\User\Desktop\data.txt

# There are two types.
# Relative path
# data.txt
# Means:
# Look for data.txt in the current working directory.


# Absolute path
# C:\Users\User\Desktop\data.txt
# Means:
# The complete location of the file.


# Opening a File
# Python uses:
# open()

# Basic structure:
# file = open("data.txt", "r")

# Think:
# open(
#     file name,
#     mode
# )
# Here:
# data.txt → file name
# r        → read mode