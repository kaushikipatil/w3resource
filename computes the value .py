"""
10. Write a Python program that accepts an integer (n) and computes the value
of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
"""

print("Enter the number")
n=int(input())
print("Sample value of n is ",n)

addition=int(0)
multiply=int(0)

for i in range(0,n):
    addition+=n
    multiply+=(addition*10)+n
    print(addition)
