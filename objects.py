
'''OBJECTS
(1) What is object
(2) Iterable objects & RANGE
(3) DICTIONARY
(4) Error handling system
'''
import array  # package/module
import math
from math import ceil
print("======== (1) What is object ========")
# An object has state and method properties.
# Everything is object in Python!

print(type("Hello World"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & OOP
# OOP 4 concepts > Abstraction | Encapsulation | Inheritance | Polimorhism
result1 = math.ceil(97.7)  # Call
print("result:", result1)

result2 = ceil(98.7)
print("result2:", result2)


print("======== (4) Error handling system ========")

car_dict = dict(name="Tayota", year=2026, electric=True)

try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print("result:", result)
# 1) except KeyError as err:
#     print("No origin state property found:", err)
# except AttributeError as err:
#     print("No spped found:", err)

# 2)except (KeyError, AttributeError) as err:
#   print("Error:", err)
except Exception as err: #hamma hatoliklarni chiqaradi
    print("general result:", err)
else:  # umuman hato bolmaganda yuradi
    print("Executed successfully without errors")
finally:  # mantiqda hatolik boladi yoqmi baribir ishga tushadi
    print("Final closing logic")
