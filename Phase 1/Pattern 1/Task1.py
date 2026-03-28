'''🏋️ Practice Exercises — Do These Now, Without AI Help
Exercise 1 — Strict: Write a BankAccount class from scratch with:

Class attribute bank_name = "NationalBank"
__init__ taking owner and balance
A deposit(amount) method that increases balance
A withdraw(amount) method that raises a ValueError if balance is insufficient
A __repr__ that returns something like BankAccount(owner=Yash, balance=5000)

Exercise 2 — Inheritance: Write an Animal base class, then a Dog class that inherits from it. Animal should have a speak() method. Dog should override it.
Exercise 3 — Tricky: Demonstrate the class-vs-instance attribute shadowing bug I described above. Write code that shows the difference in behavior.'''
#Exercise 1
class BankAccount():
    bank_name = "National Bank"
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return f"New Balance after crediting {amount} is {self.balance}"
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"Insufficient balance. Available: {self.balance}, Requested: {amount}")
        else:
            self.balance -= amount
            return f"New Balance after debiting {amount} is {self.balance}"
    def __repr__(self):
        return f"BankAccount Information {self.bank_name, self.owner, self.balance}"
    
c1 = BankAccount("Yash", 25_000)
a = c1.deposit(10_000)
b = c1.withdraw(25_000)
print(a,b,c1, sep= "\n")

# Exercise 2
class Animal:
    def speak(self):
        return "Some generic animal sound"   

class Dog(Animal):
    def speak(self):                         
        return "Bark"

class Cat(Animal):
    def speak(self):                         
        return "Meow"

dog = Dog()
cat = Cat()
print(dog.speak())   
print(cat.speak())   

#Exercise 3
class Country():
    location = "Globe"
class India(Country):
    location = "Asia"
obj = India()
print(obj.location)
print(Country.location)