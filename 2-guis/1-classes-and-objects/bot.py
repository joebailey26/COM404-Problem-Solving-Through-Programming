#this is a class (blue print)
class Bot:
  def __init__(self, name, age=0, energy=0, shield=0):
    self.name = name
    self.age = age
    self.energy = energy
    self.shield = shield

  def display_name(self):
    print("The name is {}".format(self.name))

  def display_age(self):
    print("The age is {}".format(self.age))

  def display_energy(self):
    print("The energy level is {}".format( self.energy))

  def display_shield(self):
    print("The shield level is {}".format(self.shield))

  def display_summary(self):
    print("{} is {} years old, their energy level is {}, and their shield level is {}".format(self.name, self.age, self.energy, self.shield))

  def __str__(self):
    return (self.name, self.age, self.energy, self.shield)
