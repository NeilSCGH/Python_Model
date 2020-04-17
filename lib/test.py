import numpy as np

class MyClass():
  def __init__(self):
    self.name ="neil"

    print(self._init())
    self._printName()

  def _init(self):
    self.age = 21
    return self.age

  def _printName(self):
    print(self.name)