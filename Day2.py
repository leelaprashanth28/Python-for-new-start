''' Datatypes in Python'''
"""Datatypes in python are classified as 'int' for integer data, 'float' for decimal data, 'complex' for complex numbers
'use complex( x, y)', 'string' for character data and collection datatypes such as 'list' for for listing any type of different datas in a 
single variable, 'tuple' for storiing different types of data in a single variable. The list and tuple are similar 
to eachother except for the mutability where the list is immutable(data can't be altered) and tuple is
mutable(data can be altered). Dictionary is another datatype in which the data can be stroed as key : value pair
where the key and value data need not be similar datatypesand the key data is unique and the value data can be duplicate"""

a = 5 # integer
b = -1.10 # float
c = complex( 8, 5) # complex number
d = "Prashanth"
e = [8, 6.5, ['and', 5]]
f = (7, complex(1, 1), (50, 'Hin'))
g = {'Name' : 'Adhishek', 'Rate': 23}
print(a, b, c, d, e, f, g, sep = "\n")