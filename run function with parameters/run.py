import sys
import os

from lib.tools import *
from lib.person import *

if __name__ == '__main__':
	tool = tools(sys.argv)
	pers=person(sys.argv)
	
	pers.run()
	#if tool.argExist("-aff"):
	#	val=tool.argValue("-aff")
	#	functions.aff(val)

	#if tool.argExist("-dbl"):
	#	val=tool.argValue("-dbl")
	#	functions.dbl(val)