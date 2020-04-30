class tools():
  def __init__(self, args):
    self.args = args

  def argExist(self,argName): #check if the argument is provided
    if argName not in self.args:
    	#print(argName,": Unknown")
    	return False

    indx=self.args.index(argName)
    if indx+1 == len(self.args): #if the argName is the last element
    	#print(argName,": Missing value")
    	return False

    return True

  def getArgs(self): #get all the args
    return self.args

  def argValue(self,argName): #extract the value of the argument
    indx=self.args.index(argName)
    return self.args[indx+1]

  def validValue(self,argName): #extract the value of the argument
    return self.argExist(self.argValue(argName))