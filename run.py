import sys
import os

from lib.ArgumentParser import *

class Program(object):
    def __init__(self):
        self.script_path = (os.path.dirname(os.path.realpath(__file__)))
        self.arguments = ArgumentParser(self.script_path)

if __name__ == '__main__':
  main=Program()
  print(os.path.realpath(__file__))
  print(main.script_path)
  print(main.arguments.data)