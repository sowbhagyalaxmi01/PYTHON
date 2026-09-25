# #A Python package is a collection of Python modules organized in a folder. Packages help us reuse code and organize large programs.
# # A module is usually one .py file.
# # A package is a directory containing multiple modules.
# # A library is a broader term for reusable code, often made up of one or more packages.




# # Why are packages used?
# # Packages are mainly used for:
# # Code reuse — use existing code instead of writing everything again.
# # Organization — divide a large project into smaller parts.
# # Maintainability — make code easier to update and debug.
# # Sharing — package code can be shared with other developers.
# # Adding functionality — third-party packages provide ready-made features.


# # types of packages
# #NumPy (Numerical Python) is a package used for numerical calculations, arrays, matrices, and mathematical operations.
# Install:
# pip install numpy
# Example:
# import numpy as np
# numbers = np.array([10, 20, 30, 40])
# print(numbers)
# print(numbers * 2)

# Output:
# [10 20 30 40]
# [20 40 60 80]
# Used for: Data science, mathematics, scientific computing.


# 2. Pandas
# Definition:
# Pandas is a package used for data analysis and manipulation. It works especially well with tables, CSV files, and datasets.
# Install:
# pip install pandas
# Example:
# import pandas as pd
# data = {
#     "Name": ["John", "Alice", "Bob"],
#     "Age": [20, 25, 22]
# }

# df = pd.DataFrame(data)
# print(df)
# Output:
#     Name  Age
# 0   John   20
# 1  Alice   25
# 2    Bob   22

# Used for: Data analysis, CSV/Excel data, data cleaning.



# 3. Matplotlib
# Definition:
# Matplotlib is a package used to create graphs, charts, and visualizations.
# Install:
# pip install matplotlib
# Example:
# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4]
# y = [10, 20, 15, 30]
# plt.plot(x, y)
# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.title("My Graph")
# plt.show()
# Used for: Line graphs, bar charts, pie charts, data visualization.



# 4. Requests
# Definition:
# Requests is a package used to send HTTP requests to websites and APIs.
# Install:
# pip install requests
# Example:
# import requests
# response = requests.get("https://example.com")
# print(response.status_code)
# A status code such as 200 generally means the request was successful.
# Used for: APIs, websites, downloading web data.


# 5. Beautiful Soup
# Definition:
# Beautiful Soup is a package used to extract and parse information from HTML and XML documents.
# The package is installed as:
# pip install beautifulsoup4
# Example:
# from bs4 import BeautifulSoup
# html = """
# <html>
#     <body>
#         <h1>Hello Python</h1>
#         <p>This is my website.</p>
#     </body>
# </html>
# """
# soup = BeautifulSoup(html, "html.parser")
# print(soup.h1.text)
# print(soup.p.text)
# Output:
# Hello Python
# This is my website.
# Used for: HTML parsing and web scraping.



# 6. Flask
# Definition:
# Flask is a lightweight Python web framework used to create web applications and APIs.
# Install:
# pip install flask
# Example:
# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def home():
#     return "Hello, World!"
# app.run()
# When you run the program, Flask starts a web server.
# Used for: Websites, REST APIs, small-to-medium web applications.



# 7. Django
# Definition:
# Django is a Python web framework designed for building larger and feature-rich web applications.
# Install:
# pip install django
# A Django project can be created with:
# django-admin startproject mysite
# Used for: Large websites, authentication systems, databases, admin panels, APIs, etc.
# Django is more of a framework than just a small utility package.




# 8. Scikit-learn
# Definition:
# Scikit-learn is a package used for machine learning.
# Install:
# pip install scikit-learn
# Example:
# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# X = [[1], [2], [3], [4]]
# y = [2, 4, 6, 8]
# model.fit(X, y)
# print(model.predict([[5]]))
# Output will be approximately:
# [10.]
# Used for: Classification, regression, prediction, clustering, and machine learning.



# 9. OpenPyXL
# Definition:
# OpenPyXL is a package used to read and write Microsoft Excel .xlsx files.
# Install:
# pip install openpyxl
# Example:
# from openpyxl import Workbook
# workbook = Workbook()
# sheet = workbook.active
# sheet["A1"] = "Name"
# sheet["B1"] = "Age"
# sheet["A2"] = "John"
# sheet["B2"] = 20
# workbook.save("students.xlsx")
# This creates an Excel file called:
# students.xlsx
# Used for: Excel automation, reading and writing spreadsheets.



# 10. TensorFlow
# Definition:
# TensorFlow is a framework used for machine learning and deep learning.
# Install:
# pip install tensorflow
# Simple example:
# import tensorflow as tf
# x = tf.constant([1, 2, 3])
# y = tf.constant([4, 5, 6])
# print(x + y)
# Used for: Neural networks, deep learning, image recognition, natural language processing, etc.



# 11. PyTorch
# Definition:
# PyTorch is a machine-learning framework commonly used for deep learning and neural networks.
# Example:
# import torch
# x = torch.tensor([1, 2, 3])
# y = torch.tensor([4, 5, 6])
# print(x + y)
# Output:
# tensor([5, 7, 9])
# Used for: Deep learning, neural networks, computer vision, and AI research.



# 12. Seaborn
# Definition:
# Seaborn is a data visualization package built on top of Matplotlib. It makes it easier to create attractive statistical graphs.
# Install:
# pip install seaborn
# Example:
# import seaborn as sns
# import matplotlib.pyplot as plt
# data = [10, 20, 20, 30, 40, 40, 40, 50]
# sns.histplot(data)
# plt.show()
# Used for: Statistical graphs and data visualization.



# Quick revision table
# Package	Definition	                   Main use
# NumPy	Numerical computing package 	Arrays & mathematics
# Pandas	Data manipulation package	   Data analysis
# Matplotlib	Visualization package	   Graphs & charts
# Requests	HTTP package            	APIs & web requests
# Beautiful Soup	HTML/XML              parser	Web scraping
# Flask	Web framework               	Web apps & APIs
# Django	Full web framework           	Large web applications
# Scikit-learn	Machine-learning package 	ML algorithms
# OpenPyXL	Excel package	            Excel automation
# TensorFlow	ML/deep-learning framework  	AI & neural networks
# PyTorch	Deep-learning framework	    AI & neural networks
# Seaborn	Visualization package	      Statistical graphs

# Easy way to remember
# NumPy       → Numbers
# Pandas      → Data
# Matplotlib  → Graphs
# Requests    → Internet/API
# BeautifulSoup → Web scraping
# Flask       → Web apps
# Django      → Large web apps
# Scikit-learn → Machine Learning
# OpenPyXL    → Excel
# TensorFlow  → Deep Learning
# PyTorch     → Deep Learning
# Seaborn     → Statistical graphs



