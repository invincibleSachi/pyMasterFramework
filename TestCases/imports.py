import os
from os.path import dirname as up
from os.path import exists, join
import sys

currentFile = os.path.abspath(__file__)

projectPath = up(up(up(currentFile)))
testingPath = join(projectPath, "testing")
testingPath = join(projectPath, "testing/TestCases")
sys.path.append(projectPath)
sys.path.append(testingPath)
sys.path.append(join(projectPath, "src"))

import constants

