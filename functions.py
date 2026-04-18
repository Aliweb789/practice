'''
Functions
    (1) DEFINE vs CALL
    (2) Parameter vs Argument
    (3) Keyword & default arguments
    (4) Scope
'''

print("====== DEFINE (parameter) vs CALL (argument)=======")
# build in function > print() type()
# Function - resuable block of code!
# Instead of block {} in JAVA, Python uses indentation!

# DEFINE - build(parameter)
def greet(a):
    # pass (hech narsa qilma)
    print(f"How do you do, {a}")

def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"
# f"ss" --> format string
# CALL - execute(argument)
# None --> javascriptdagi undefined hisoblanadi

result1 = greet("Martin")
print("result1:", result1)  # --> console da none chiqadi
# greet("Martin")
result2 = greeting('Justin')
print("result2:", result2)

print("====== Keyword & default arguments =======")

# DEFINE
def give_greet(name, age = 22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old"

#CALL
result3 = give_greet(name = 'Justin', age = 28) #keyword arguments
print("result3:", result3)

result4 = give_greet("John") #default argument(age)
print("result3:", result4)

print("====== Scope =======")
b = 100 #3

#DEFINE
def calculate(a, b): #2
    c = a + b #1
    print(f"the c value: {c}")

#CALL
calculate(5, 50)