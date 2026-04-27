''' Comprehension
    (1) What is comprehension & list comp
    (2) set and dictonary comp
'''

print("======== What is comprehension & list comp =========")
# comprehension acts like spread operator!
'''
    a) *iterable
    b) <expresiion> for item in iterable
    c) <expresiion> for item in iterable <condition>
'''

#list comp.
numbers = [1, 2, 4, 1, 2, 20] #comp qiymatlardan foydalanib butunlay yangi reference hosil qiladi
list_numbers = [*numbers]   #a version agar numbers ozi bolganda solishtirganimizda bir xil bolib true chiqadi
print("list_numbers:", list_numbers)
print(numbers is list_numbers) #hozir bu yerda false chiqadi
print(id(numbers), id(list_numbers))

print("-----------------")
people = [("Robert", 21), ("Steve", 19), ("Tony", 25)]
list_people = [person[0] for person in people] #b version
print("list_people", list_people)


cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33),
]
list_cars = [car[0] for car in cars if car[1] > 80] #c version
print("list_cars: ", list_cars)

