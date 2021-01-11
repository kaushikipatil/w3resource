"""
11. Write a Python program to print the documents (syntax, description etc.)
of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
"""

def absolute_number(a):
    return print(abs(a))

print("Enter the number")
absolute_number(int(input()))
