"""
6. Write a Python program which accepts a sequence of comma-separated numbers
from user and generate a list and a tuple with those numbers.
"""

print("We are going to Accept numbers")
seperated_number=input()
#print(seperated_number)

list=seperated_number.split(",")
print("List= ",list)

Tuple_version=tuple(list)
print("Tuple=",Tuple_version)
