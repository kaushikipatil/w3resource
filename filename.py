"""
7.Write a Python program to accept a filename from the user and print the
extension of that.
"""

print("Here we are going to check which file you want to see")
file_name=input()

name=file_name.split(".")

print("File Name is ",name[-1])
