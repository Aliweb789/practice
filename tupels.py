'''
Tupels
    (1) What is a tupel: tuple vs list
    (2) unpacking arguments
    (3) zip
'''

print("======= What is a tuple: tuple vs list =========")
#Java/PHP/NodeJs array => Python list(array), array(arraylarni biz specific hollarda katta hajmdagi ma'lumotlarni saqlash uchun ishlatamiz)

# literal 
numbs = [3, 5, 1, 2]
# car_dict = {"brand": "Ferrari", "year": 1995}
print(numbs)

# constructor 
letters = list("Hello World!")
# person_dict = dict(name="Martin", age = 35)
print(letters)

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)

#tuple => listga o'xshash, lekin o'zgarmas (immutable) ma'lumot tuzilmasi. Tuple yaratish uchun oddiygina qavslar () ishlatiladi.
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
animals[0] = "bird"