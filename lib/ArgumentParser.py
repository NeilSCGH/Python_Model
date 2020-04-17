class ArgumentParser():
  def __init__(self,script_path):
    print("We are int the __init__")
    self.data = self.extractParameters()

  def extractParameters(self):
    return "neil" #temporaire