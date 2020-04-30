from lib.tools import *

class person():
  def __init__(self,args):
    self.firstName = "firstName"
    self.lastName = "lastName"
    self.age = "age"
    self.setup(args)

  def setup(self,args):
    tool = tools(args)
    if tool.argHasValue("-f"):
      val=tool.argValue("-f")
      self.firstName=val

    if tool.argHasValue("-l"):
      val=tool.argValue("-l")
      self.lastName=val
      
    if tool.argHasValue("-a"):
      val=tool.argValue("-a")
      self.age=val

  def setFirstName(self,firstName):
    self.firstName=firstName

  def setLastName(self,lastName):
  	self.lastName=lastName

  def setAge(self,age):
  	self.age=age

  def aff(self):
    print("{} {} : {}".format(self.firstName,self.lastName,self.age))

  def run(self):
    print("Current settings for {} :".format(self.firstName))
    self.aff()
    print("Running !")