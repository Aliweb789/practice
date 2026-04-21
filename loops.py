'''
    LOOP Operators:
    (1) for
    (2) break/ else
    (3) while
'''
print("========= For operator  =========")
#iterable objects > string, dict, list, tuple, range, map, filter

text = "MIT"
numbs = [10, 7, 3, 1]
car_obj = dict(brand="Ferrari", year=2025)
range_obj = range(5) #[0,5)

for letter in "MIT": #for amali ketma ketlikni amalga oshiradi va miqdori aniq boladi
    print(f"letter: {letter}")

print("------")

for number in numbs:
    print(f"the number: {number}")
    
print("------")

for x in range_obj:
    print(f"the element: {x}")

print("------")

for key in car_obj:
    print(f"key: {key} => value: {car_obj.get(key)}")
    
print("------")

for x in range(1, 20, 5): #5-> step
    print(f"the x: {x}")
    
print("========= Break & Else  =========")
for x in range(1, 20, 5): #5-> step
    print(f"the x: {x}")
    if x > 10:
        print("reached break")
        break #majburiy to'xtatish amali break amali bajarilganda for loop to'xtaydi va else qismi bajarilmaydi lekin undan keyin yozilgan kodlar bajariladi
else :
    print("looped successfully")
    
print("========= While operator  =========")
#takrorlanishlar soni oldindan noma'lum bo'lsa while operatoridan foydalanish mumkin
numb = 40
while numb > 0:
    numb -= 10 
    print(f"the numb equals: {numb}")
    
print("------")
count = 0
while True: #javascriptdagi dowhile loopga o'xshash
    count += 1
    x = int(input("Find number:")) #input() - foydalanuvchidan ma'lumot olish uchun ishlatiladi, int() - stringni butun songa aylantiradi
    if x == 41:
        print(f"You found the number in {count} steps")
        break #breakni ishlatmasak while doimiy aylanadi
    else:
        print("Wrong, please find again!")
