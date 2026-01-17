"""" Write a program to:
1. Create a list comprehension to store squares of all numbers
2. Create a set comprehension to store only unique even numbers
3. Create a dictionary comprehension where the key is the number and the value is its cube	"""

data=[1,2,3,4,5,6,2,4]
# List
Squares=[x**2 for x in data]
print(Squares)
# Set
even_set={x for x in data if x%2==0}
print(even_set)
# Dictionary
cube_dict={x:x**3 for x in data}
print(cube_dict)