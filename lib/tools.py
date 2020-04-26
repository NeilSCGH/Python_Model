class tools():
  def __init__(self, args):
    self.args = args

  def argExist(self,argName): #check if the argument is provided
    return (argName in self.args)

  def getArgs(self): #get all the args
    return self.args

  def argValue(self,argName): #extract the value of the argument
    assert self.argExist(argName), "THIS ARG DOEN'T EXIST"
    indx=self.args.index(argName)
    assert indx+1 <= len(self.args) #if the argName is the last element
    return self.args[indx+1]