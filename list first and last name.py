"""
8.Write a Python program to display the first and last colors from the following
list
color_list = ["Red","Green","White" ,"Black"]
"""

print("Hey, Welcome to List program")

color_list=[]

print("Enter no.of elements")
n=int(input())

for i in range(0,n):
    adding=input()
    color_list.append(adding)

print(color_list)
