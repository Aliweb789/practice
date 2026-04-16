print("======== (2) Iterable objects & RANGE ========")
#Iterable objects > string dict tuple list map range filter

range_obj = range(3) #0 dan 3 gacha bolgan sonlarni chiqarib beradi [0, 3)--> 0,1,2
print("range_obj:", range_obj)


text = "MIT"
for letter in text:
    print(f"the letter: {letter}")

for ele in range_obj:
    print(f"the element: {ele}")

print("======== DICTIONARY ========")
# Dictionary is JSON object!
#objectlarni ikki hil yol bilan tuzsa boladi
person = {"name": "Justin", "age": 25, "single": True}
person_obj = dict(name = "Justin", age = 25, single = True)
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

name09 = person_obj["name"]
print("name:", name09)

#objectda yoq bolgan qiymatni print qilsak error boladi
# hobby = person_obj["hobby"]
# print("name:", hobby)

#method: get()
# name = person_obj["name"]

name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0) #qiymat yoq bolib none qaytarishni orniga 0 ni qaytar
print(f"the name: {name}, hobby: {hobby} and balance: {balance}") #agar hobby qiymati bolmasa none qaytaradi

del person_obj["single"]
for key in person_obj:
    print(f"the key: {key} => value {person_obj[key]}") #person_obj[key] -- person_obj.get(key)