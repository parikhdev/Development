class BankAccount:
    def __init__(self, balance):
        self._balance = balance  

    @property
    def balance(self):    
        if self._balance is None:
            return "This account has been closed"
        return self._balance

    @balance.setter
    def balance(self, amount):   
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount

    @balance.deleter
    def balance(self):    
        print("Alert: Closing account and wiping balance.")      
        self._balance = None


acc = BankAccount(1000)

print(acc.balance)      # calls the GETTER → 1000
acc.balance = 500       # calls the SETTER → works fine
print(acc.balance)      # calls the GETTER → 1000
del acc.balance         # calls the DELETER
print(acc.balance)

'''The Temperature class I described. Here's the requirements again briefly:

_celsius stored internally
celsius property with getter + setter (reject below -273.15)
fahrenheit property that computes on the fly — read only, no setter
__repr__ showing both values

You have everything you need from my explanation. Attempt it now.'''

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    @property
    def fahrenheit(self):
        return round((self._celsius * 9/5) + 32, 4)
    @property 
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self,value):
        if value >= -273.15:
            self._celsius = value
        else:
            raise ValueError("Celsius can't be lower than -273.15")
    def __repr__(self):
        return f"The Temperature in Celsius is {self._celsius} and Fahrenheit is {self.fahrenheit}"
temp = Temperature(33)
print(temp.fahrenheit)
temp.celsius = 200
print(temp.celsius)  
print(temp)
temp.celsius = -300