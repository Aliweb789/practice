'''
CLASS DEEP DIVING
    (1) ENCAPSULATION
    (2) INHERITANCE
    (3) POLOMORHISM
'''

print("--------- Encapsulation ----------")
# Encapsulation > public _protected __private

class Account:
    #state
    description = "The class makes bank accounts"
    #constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount
    #methods
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")
    
    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount
    @property #method singari emas state singari ishlaydi
    def holder(self): #getter
        return self.__owner
    
    @holder.setter #setter
    def holder(self, new_owner):
        print("holder setter:", new_owner)
        self.__owner = new_owner


    def change_ownership(self, new_owner): #settersiz ozgartirishda
        print("change ownership:", new_owner)
        self.__owner = new_owner



my_account = Account("Shawn", 1000)
my_account.get_balance()
print("---------")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

print("---------")
# my_account.amount = 1000000
# my_account.owner = "Martin"
# my_account.get_balance()

try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("No target state found:", err)


# account_owner = my_account.holder #state
print("owner before:", my_account.holder) #state

# my_account.change_ownership("Martin") #setter ishlatmasdan ozgartirishda
my_account.holder = "Martin" #setter orqali ozgartirishda(state)
print("owner after:", my_account.holder) #state