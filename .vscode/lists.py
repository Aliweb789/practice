''' List
    (1) Working with lists
    (2) List methods
    (3) lambda sunctions
    (4) enumerate, map and filter
'''

print("========= working with lists ===========")
#Java/PHP/NodeJs array => Python list


# literal
person = {"name": "Justin", "age": 25} #dictionary
people = ("Andrew", "John", "Michael") # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"] # list

for team in groups:
    print(f"the team: {team}")
    
    
#constructor
result = list("Hello World!")
print(f"the letters: {result} and size: {len(result)}")


print("=======")
fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2] #0dan boshlab 2 ga qadar qiymatlarni olib ber [0, 2)
c = fruits[::3] #0dan boshlab 3 qadam tashlab qiymatni oladi [0, 3, 6, 9, ...]
d = fruits[::-1] #listni teskari tartibda qaytaradi

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("========= List methods ===========")
#methods > append(), inset(), pop(), remove(), clear(), sort(),          "index()-->immutable"

letters = ["a", "d", "b"]

letters.append("c") #add behind
print(f"the append letters: {letters}")

letters.insert(0, "z") #add front
print(f"the insert letters: {letters}")

size = len(letters) - 1
result1 = letters.pop(size) #pop behind
print(f"the pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0) #pop front
print(f"the pop result2: {result2} and letters: {letters}")


print("----------")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")
print("animals remove:", animals)

del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")
print("cat exist:", exist)

animals.clear()
print("animals clear:", animals)

if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")
    
print("---------")
numbers = [2, 20, 12, 8, 57]
numbers.sort() 
print("sort default:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)

#immutable > sorted function & index() method
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new numbs: {new_numbs}")