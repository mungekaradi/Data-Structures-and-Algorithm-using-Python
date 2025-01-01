# one dimensional Array
import array as arr
a= arr.array('i',[1,2,3])
print("The new created array is: ",end=" ")
for i in range(0,3):
    print(a[i],end=" ")
print()

# Adding elements to a array
import array as arr
a= arr.array('i',[1,2,3])
print("Array before insertion: ",end=" ")
for i in range(0,3):
    print(a[i],end=" ")
print()
a.insert(1,4)
print("Array after insertion: ",end=" ")
for i in (a):
    print(i,end=" ")
print()

# Accessin Elements from the Array
import array as arr
a= arr.array('i',[1,2,3,4,5,6])
print("Access element is: ",a[0])
print("Access element is: ",a[3])
b= arr.array('d',[2.5,3.2,3.3])
print("Access element is: ",b[1])
print("Access element is: ",b[2])

# Removing Elements from the Array
import array
arr= array.array('i',[1,2,3,4,5])
print("The new created array is: ",end=" ")
for i in range(0,5):
    print(arr[i],end=" ")

print("\r")
print("The popped element is: ",end=" ")
print(arr.pop(2))
print("The array after popping is: ",end=" ")
for i in range(0,4):
    print(arr[i],end=" ")

print("\r")
arr.remove(1)
print("The array after removing is: ",end=" ")
for i in range(0,3):
    print(arr[i],end=" ")

# Searching element in a Array
import array
arr= array.array('i',[1,2,3,1,2,5])
print("The new created array is: ",end=" ")
for i in range(0,6):
    print(arr[i],end=" ")

print("\r")
print("The end of the 1st occurence of 2 is: ",end=" ")
print(arr.index(2))
print("The index of 1st occurence is: ",end=" ")
print(arr.index(1))

# Updating elements in a Array
import array
arr= array.array('i',[1,2,3,1,2,5])
print("Array before updation: ",end=" ")
for i in range(0,6):
    print(arr[i],end=" ")

print("\r")
arr[2]=6
print("Array after updation: ",end=" ")
for i in range(0,6):
    print(arr[i],end=" ")
print()
arr[4]= 8
print("Array after updation: ",end=" ")
for i in range(0,6):
    print(arr[i],end=" ")

    
