import sys
import os

from lib.ArgumentParser import *

class Program(object):
    def __init__(self):
        self.script_path = (os.path.dirname(os.path.realpath(__file__)))
        self.arguments = ArgumentParser(self.script_path)

if __name__ == '__main__':
  print("We are int the __main__")
  main=Program()
  print(main.arguments.data)