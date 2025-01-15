# Base class for Animals
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Dog class implementing move
class Dog(Animal):
    def move(self):
        print("The dog is running 🐕")

# Cat class implementing move
class Cat(Animal):
    def move(self):
        print("The cat is walking 🐈")

# Bird class implementing move
class Bird(Animal):
    def move(self):
        print("The bird is flying 🐦")

# Function to demonstrate polymorphism
def demonstrate_move(animal):
    animal.move()

# Create instances of Dog, Cat, and Bird
dog = Dog()
cat = Cat()
bird = Bird()

# Call move() on each object (polymorphism in action)
demonstrate_move(dog)
demonstrate_move(cat)
demonstrate_move(bird)
