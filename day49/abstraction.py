#Abstraction is process in which it hides complex implementation only shows process(functionality)


#You cannot create an object of an abstract class if it has an unimplemented abstract method.
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


animal = Animal()


#Real-World Example — Payment
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print("Paid", amount, "using UPI")


class CreditCard(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


p1 = UPI()
p1.pay(500)

p2 = CreditCard()
p2.pay(1000)


