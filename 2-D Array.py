# Accessing single element
arr = [[1,2,3],[4,5,6],[7,8,9]]     
print("Element at [1][0]= ",arr[1][0])

# Accessing an internal Array
arr = [[1,2,3],[4,5,6],[7,8,9]]
print("Element at [2]= ",arr[2])        

# Traversing values in Python 2-D Array
arr = [[1,2,3],[4,5,6],[7,8,9]]         
for _ in arr:
    for i in _:                     
        print(i,end=" ")
print()

# Inserting an Array in a 2-D Array
from array import *                     

arr = [[1,2,3],[4,5,6],[7,8,9]]
                                    
print("Original Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
print()

arr.insert(2,[11,12,13])

print("Modified Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
print()

# Updating a single element
arr = [[1,2,3],[4,5,6],[7,8,9]]

print("Original Array")             
for _ in arr:
    for i in _:
        print(i,end=" ")
print()

arr[1][2]=16

print("Modified Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
print()

# Deleting values in Python 2-D Array
from array import *

arr = [[1,2,3],[4,5,6],[7,8,9]]

print("Original Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
print()

del(arr[1][2])

print("Modified Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
print()
    


