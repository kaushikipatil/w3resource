"""
Write a Python program which accepts the user's first and last name and print
them in reverse order with a space between them.
"""

print("We are going to Prrint your name in reverse order with a space")

print("Enter your First Name")
f_name=input()

print("Enter your Last Name")
l_name=input()

print(f_name[::-1]," ",l_name[::-1])
