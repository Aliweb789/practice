'''OPERATORS AND CONDITIONS
    (1) Operators
    (2) Conditions
    (3) Logical Operators
'''

print("========= Operators  =========")
# + - > < >= <= == * / %  // += -= **

a = 19
b= 5

result = a // b #bolgandagi butun qismi
left = a % b  #bolgandagi qoldiq
print(f"result: {result} and left: {left}")

# a = a + 100
a += 100
print("a:", a)

print("b**2", b**2) #b ning kvadrati
print("b**3", b**3) #b ning kubi

# print("=====")
print("="*5)

c = dict(name="Martin", age=35)
d = dict(name="Martin", age=35)
e = c #reference va valueni beradi

print("c == d:", c == d) #== ->referensiya emas qiymatni solishtiradi
print(id(c), id(d), id(e)) #id() - obyektning unikal identifikatori

# data = c is d #is -> referensiyani solishtiradi, c va d bir xil obyektga ishora qiladimi
print("c is d:", c is d)
print("c is e:", c is e)
