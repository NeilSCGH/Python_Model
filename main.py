import sys

from lib.utils import *
utils.checkRequirements(["numpy"])

class person():
  def __init__(self,args):
    self.utils = utils(args)
    self.setup(args)

  def setup(self,args):
    if self.utils.argExist("-h"):
      self.help()
      exit(0)

    if self.utils.argHasValue("-f"):
      self.firstName=self.utils.argValue("-f")
    else:
      print("Firstname is missing !")
      self.help()
      exit(1)

    if self.utils.argHasValue("-l"):
      self.lastName=self.utils.argValue("-l")
    else:
      self.lastName = "Doe"

    if self.utils.argHasValue("-a"):
      try:
        self.age=int(self.utils.argValue("-a"))
        assert self.age >= 0
      except:
        print("Invalid age !")
        exit(1)
    else:
      if self.utils.argExist("-adult"):
        print("Check if adult requested but no age provided !")
        exit(1)
      else:
        self.age = 0


  def help(self):
  	print("")
  	print("Usage: python main.py -f firstname [-l lastname] ")
  	print("                      [-a age] [-adult] [-h]")
  	print("")
  	print("Options:")
  	print("   -f firstname First name.")
  	print("   -l lastname  (Optional) Last name, default: \"Doe\".")
  	print("   -a age       (Optional) Age.")
  	print("   -adult       (Optional) Check is the person is adult.")
  	print("                Require -a.")
  	print("   -h           (Optional) Print this help.")
  	print("")

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

    if self.utils.argExist("-adult"):
      self.checkIfAdult()


if __name__ == '__main__':
	pers = person(sys.argv)
	pers.run()