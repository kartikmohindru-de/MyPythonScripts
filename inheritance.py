class animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")

class dog(animal): #inheritance
    def __init__(self):
        animal.__init__(self)
        print("Dog created")
    def who_am_i(self): #overriding
        print("I am dog")
    def bark(self):
        print("woof")

mydog = dog()

mydog.who_am_i()
mydog.eat()
mydog.bark()