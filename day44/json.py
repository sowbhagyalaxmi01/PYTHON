#JSON in Python
# JSON means JavaScript Object Notation. It is commonly used to store and exchange data.
# Python has a built-in json module.

#Python dictionary → JSON string
import json
data = {
    "name": "Sowbhagya",
    "age": 20
}
x = json.dumps(data)
print(x)

#JSON string → Python dictionary
import json
x = '{"name": "Sowbhagya", "age": 20}'
data = json.loads(x)
print(data["name"])#sowbhagya

#Remember:
# json.dumps() → Python → JSON
# json.loads() → JSON → Python