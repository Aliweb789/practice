''' Array & set
    (1) Array
    (2) Set
    (3) Specific operators with set
'''
from array import array
print("========= Array =========")

numbers = array("i", [1, 4, 5, 7, 8, 41])
print("numbers(1):", numbers)

numbers.append(100)
numbers.insert(0,14)
print("numbers(2):", numbers)

numbers.remove(5)
numbers.pop()
print("numbers(3):" , numbers)

del numbers[0:2]
print("numbers(4):", numbers)

print("========= Set =========")
# {set} of unique collection without keeping order!
new_numbers = array("i", [1, 4, 5, 7,  5, 7, 8, 4, 41])
numb_set = set(new_numbers) #sonlar takrorlanmaydi

print(f"numbs_set: {numb_set} and type {type(numb_set)}")


numb_set.add(200)
print("numbs_set(1):", numb_set)

numb_set.add(7) #7 soni borligi sababli qoshmaydi
print("numbs_set(1):", numb_set)


print("========= Specific operators: | & - ^  =========")
# | & - ^
a = {10, 20, 50}
b = {20, 40}

result1 = a | b #union bir xil bolgan qiymatlarni olmay birlashtirib beradi
result2 = a & b #intersection bir xil sonlar
result3 = a - b #difference (qoshish ayirishga oxshaydi)
result4 = a ^ b #symmetric difference (bir birida qaytalanmagan raqamlarni chiqarib beradi)

print("result1:", result1)
print("result2:", result2)
print("result3:", result3)
print("result4:", result4)
