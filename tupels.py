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
# animals[0] = "bird"

# try avoid this
# people = "Andrew", "John"
# animals = "dog",
# x, y, z, a = groups

print("======= unpacking arguments =========")
groups = ["MIT", "Mashaqqat", "Flexy", "Devex", "MG"]
(x, y, *z) = groups #*z qolganelementlarni oziga oladi
print(f"the x: {x}, the y: {y}")
print("z:", z) #list


# *args > tuple
def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


#call
calculate(1, 7, 2, 3)
print("---------")
calculate(0, 2, 300)
calculate(5, 7)
print("---------")

#**kwargs > dictionary
def introduce(**kwargs):
    print(f"the type (**kwargs) value: {type(kwargs)}")
    print(f"Hi I am {kwargs["name"]} and I am {kwargs["age"]} years old!")

#call
introduce(name = "Justin",  age = 25)
introduce(name = "Shawn",  age = 30, single = True)
print("---------")


def greeting(*args, **kwargs): #**kwargs --> keyword arguments
    print("*args >", args)
    print("**kwargs >", kwargs)

#call
greeting("Hi", True, 10, name = "John", age = 22)

print("======= zip =========")
tuple1 = (1, 2, 3, 4)
tuple2 = ("a", "b", "c")

zipped = zip(tuple1, tuple2)
print("zipped:", zipped) #bu xolda biz zip objectni manzilini koraolamiz holos
#zip tarkibini korish uchun biz uni listga berishimiz kerak(iterable object hisoblanadi)
result = list(zipped)
print(f"the result: {result}")