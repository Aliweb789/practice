'''
CLASS DEEP DIVING
    (1) ENCAPSULATION
    (2) INHERITANCE
    (3) POLOMORHISM
'''
print("======= Inheritance ========")
#parent > child
#parent only public va protected state va methodlarni childga beradi, private state va methodlarni bermaydi

#Parent class
class Animal(): #scopeni qoymasa ham hato hisoblamaydi
    description = "This class is parent for animals"

    def __init__(self, voice):
        self._status = "animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal): #child class

    def __init__(self,name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice) #super() > parent classni chaqirish uchun


    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you")
    

class Cat(Animal): #child class

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice) #super() > parent classni chaqirish uchun

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal): #child class

    def __init__(self,name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice) #super() > parent classni chaqirish uchun

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        pass

dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "Zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("----------------------------------")
dog.make_voice()

print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print("dog.status:", dog._status)
print("cat.status:", cat._status)
