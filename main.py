#MULTILEVEL INHERITANCE
class Animal:

  def __init__(self, name, type):
    self.name = name
    self.type = type

  def show(self):
    print(f"Animal name: {self.name}")
    print(f"Animal type: {self.type}")


class Dog(Animal):

  def __init__(self, name, breed):
    super().__init__(name, type="Dog")
    self.breed = breed

  def show(self):
    super().show()
    print(f"Dog breed: {self.breed}")


class Bulldog(Dog):

  def __init__(self, name, color):
    super().__init__(name, breed="Bulldog")
    self.color = color

  def show(self):
    super().show()
    print(f"Dog color: {self.color}")


b = Bulldog("Tommy", "White")
b.show()