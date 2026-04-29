'''Packages & Debugging
    (1) Python Packages & Core Package
    (2) Package Manager & External package
    (3) Debugging
'''

print("============= Python Packages & Core Package ==========")

''' Python packages/modules: Core, File and External'''
#Core packages > https://docs.python.org/3/library

from PIL import Image
import turtle
#Core forward(100) left(100) 
t = turtle.Turtle()
t.shape("turtlef")
t.speed(1)
t.circle(100)

turtle.done()

print("=======")
#doimo fayllar ochilgandan keyin yopilishi kerak
my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()

#with --> ozi faylni yopib beradi va biz kop ishlatamiz
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your content:", your_content)
print("Done")

print("============= Package Manager & External package ==========")
'''package manager -->
    Python > pip pienv
    NodeJs > npm yarn
    PHP > composer
    MacOs > brew
'''
# External packages --> https://pypi.org

with Image.open("material/googleLogo.png") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")

print("============= Debugging==========")

def get_summary(*args): # DEFINE
    total_amount = 0
    for a in args:
        total_amount += a
        return total_amount #find the bug via debugging

# CALL
test = 100
result = get_summary(1, 2, 3, 4, 5)
print("result:", result)