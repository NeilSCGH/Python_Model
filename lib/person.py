from lib.tools import *

class person():

  def __init__(self,args):
    self.tool = tools(args)
    self.setup(args)

  def setup(self,args):
    if self.tool.argExist("-h"):
      print("help msg")
      exit(0)

    if self.tool.argHasValue("-f"):
      self.firstName=self.tool.argValue("-f")
    else:
      self.firstName = "John"

    if self.tool.argHasValue("-l"):
      self.lastName=self.tool.argValue("-l")
    else:
      self.lastName = "Doe"

    if self.tool.argHasValue("-a"):
      try:
        self.age=int(self.tool.argValue("-a"))
        assert self.age >= 0
      except:
        print("Invalid age !")
        exit(1)
    else:
      self.age = 0

  def print(self):
    print("{} {} is {} years old".format(self.firstName,self.lastName,self.age))

  def checkIfAdult(self):
    if self.age >= 18:
      print("{} {} is adult".format(self.firstName,self.lastName))
    else:
      print("{} {} is NOT adult".format(self.firstName,self.lastName))

  def run(self):
    print("Running !")
    self.print()

    if self.tool.argExist("-adult"):
      self.checkIfAdult()