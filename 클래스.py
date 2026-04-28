lass Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"
    
class Dog(Animal):
    def speak(self):
        return F" {self.name} says Woof!"
    
class Cat(Animal):
    def speak(self):
        return F" {self.name} says Meow!"
    
my_dog = Dog(name="Buddy")
my_cat = Cat(name="Whiskers")

print(my_dog.speak())  # Output: Buddy says Woof!
print(my_cat.speak())  # Output: Whiskers says Meow!
