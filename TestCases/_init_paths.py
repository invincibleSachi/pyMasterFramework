import os
import sys
from os.path import dirname as up
from os.path import join

currentFile = os.path.abspath(__file__)

arojectPath = up(up(up(currentFile)))
projectSrc = join(arojectPath, 'src')
testingPath = join(arojectPath, 'testing')

sys.path.append(arojectPath)
sys.path.append(projectSrc)
sys.path.append(testingPath)
sys.path.append(join(testingPath, 'TestCases'))

import pytest
import constants
from testutils.data import refresh_dir
