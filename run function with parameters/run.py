import sys
import os

from lib.tools import *
from lib.functions import *

if __name__ == '__main__':
	tool = tools(sys.argv)

	if tool.argExist("-aff"):
		val=tool.argValue("-aff")
		functions.aff(val)

	if tool.argExist("-dbl"):
		val=tool.argValue("-dbl")
		functions.dbl(val)