# # A poymorphism is an OOP features or method and it allows to access the same method and thay act differently according to their object


# # Method overriding
# class Dog:
#     def bark(self):
#         print("Dog is barking")


# class Cat(Dog):
#     def bark(self):
#         print("Cat are doing meow")


# cat = Cat()
# dog = Dog()

# cat.bark()
# dog.bark()


# # Duck typing
# class Duck:
#     def talk(self):
#         print("Quack")


# class Human:
#     def talk(self):
#         print("Hey, Hello")


# human = Human()
# duck = Duck()
# human.talk()
# duck.talk()


# Encapsulation
class Bank:
    def __init__(self):
        self.name = "Nishant"
        self._account = 123232323232424
        self.__balance = 100000

    def inside(self):
        print("Inside the class")
        print("Name :", self.name)
        print("Account No :", self._account)
        print("Balance :", self.__balance)


bank = Bank()

bank.inside()

print("Protected Account:", bank._account)

# Name mangling
print("Private Balance:", bank._Bank__balance)
