''' Array & set
    (1) Array
    (2) Set
    (3) Specific operators with set
'''
from array import array

numbers = array("i", [1, 4, 7, 8, 41])
print("numbers(1):", numbers)

numbers.append(100)
numbers.insert(0,14)
print("numbers(2):", numbers)